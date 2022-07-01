from rest_framework import serializers

from iam.models import User
from orders.models import Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('role', 'created_at', 'updated_at', 'password', 'last_login', 'is_staff', 'date_joined')


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'
