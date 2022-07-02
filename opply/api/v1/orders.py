from django.urls import path

from orders.views import ListOrderView, CreateOrderView

urlpatterns = [
    path('', ListOrderView.as_view(), name="list_orders"),
    path('create/', CreateOrderView.as_view(), name="create_orders"),
]