from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from products.models import Product
from products.serializers import ProductSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get',)

    def get_queryset(self):
        return Product.objects.alias(
            products_in_stock=F('product_stocks__productstock__amount_in_stock')
        ).filter(
            products_in_stock__gt=0
        ).all()
