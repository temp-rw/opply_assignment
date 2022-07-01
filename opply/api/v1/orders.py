from django.urls import path

from orders.views import ListOrderView, DeclineOrder

urlpatterns = [
    path('', ListOrderView.as_view(), name="list_create_orders"),
    path('{uuid}/decline', DeclineOrder.as_view(), name="decline_order"),
]