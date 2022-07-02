from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from iam.models import User
from orders.constants import OrderStatuses
from orders.models import Order, ProductStock, Stock
from products.serializers import ProductSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "role",
            "created_at",
            "password",
            "last_login",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
            "is_superuser",
        )


class ProductStockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductStock
        exclude = ("stock",)


class StockSerializer(serializers.ModelSerializer):
    product_stock = ProductStockSerializer(source="productstock_set", many=True)

    class Meta:
        model = Stock
        fields = "__all__"


class ListOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    stock = StockSerializer()

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {"status": {"read_only": True}}


class CreateOrderSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    stock_id = serializers.CharField()
    amount = serializers.IntegerField(min_value=1)
    amount_left_in_stock = serializers.ReadOnlyField()

    def to_internal_value(self, data):
        user = self.context["request"].user
        data["customer"] = CustomerSerializer(user).data["uuid"]
        return super().to_internal_value(data)

    def validate(self, attrs):
        stock_product = ProductStock.objects.filter(stock_id=attrs["stock_id"], product_id=attrs["product_id"]).first()
        if stock_product.amount_in_stock < attrs["amount"]:
            raise ValidationError(
                {"amount": "You can't buy more products then exists in store"}, code=status.HTTP_400_BAD_REQUEST
            )
        return attrs

    def create(self, validated_data):
        customer_id = self.context["request"].user.uuid
        stock_product = ProductStock.objects.filter(
            stock_id=validated_data["stock_id"], product_id=validated_data["product_id"]
        ).first()
        order = Order.objects.create(
            stock_id=validated_data["stock_id"], customer_id=customer_id, status=OrderStatuses.RESERVED
        )
        new_product_amount = stock_product.amount_in_stock - validated_data["amount"]
        ProductStock.objects.update(
            stock_id=validated_data["stock_id"],
            product_id=validated_data["product_id"],
            amount_in_stock=new_product_amount,
        )
        validated_data["amount_left_in_stock"] = new_product_amount
        return validated_data
