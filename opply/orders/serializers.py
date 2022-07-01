from rest_framework import serializers

from iam.models import User
from orders.models import Order, ProductStock, Stock
from products.serializers import ProductSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'role',
            'created_at',
            'password',
            'last_login',
            'is_staff',
            'date_joined',
            "groups",
            "user_permissions",
            "is_superuser",
        )


class ProductStockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='productstock_set__product')

    class Meta:
        model = ProductStock
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    product_stock = ProductStockSerializer(source='productstock_set', many=True)

    class Meta:
        model = Stock
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    stock = StockSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data["products"]


class DeclineOrderSerializer(OrderSerializer):

    def create(self, validated_data):
        validated_data["products"]
