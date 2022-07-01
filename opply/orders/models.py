from django.core.validators import MinValueValidator
from django.db import models

from base.db.constants import PRODUCT_NAME_MAX_LENGTH
from base.db.models import AbstractBaseModel
from iam.models import User
from orders.constants import OrderStatuses
from products.models import Product


class Order(AbstractBaseModel):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(choices=OrderStatuses.get_choices(), max_length=30)
    stock = models.ForeignKey(to='orders.Stock', on_delete=models.SET_NULL, null=True)


class Stock(AbstractBaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    stock_products = models.ManyToManyField(
        to=Product,
        through='orders.ProductStock',
        through_fields=['stock', 'product']
    )


class ProductStock(AbstractBaseModel):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(to=Stock, on_delete=models.CASCADE)
    amount_in_stock = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    class Meta:
        unique_together = ['product', 'stock']


class OrderedProduct(AbstractBaseModel):
    original_product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH)
    price = models.FloatField()
