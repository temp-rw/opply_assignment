from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import ListOrderSerializer, CreateOrderSerializer


class ListOrderView(ListCreateAPIView):
    serializer_class = ListOrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('get',)

    def get_queryset(self):
        return Order.objects.filter(
            customer=self.request.user
        ).select_related(
            'customer',
            'stock'
        ).prefetch_related(
            'stock__productstock_set',
            'stock__productstock_set__product'
        )


class CreateOrderView(CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('post',)
