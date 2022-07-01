from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from orders.constants import OrderStatuses
from orders.models import Order
from orders.serializers import OrderSerializer


class ListOrderView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'post')

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).select_related('customer')


class DeclineOrder(UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ('post',)

    def get_queryset(self):
        return Order.objects.filter(
            customer=self.request.user,
            status=OrderStatuses.RESERVED.value
        )
