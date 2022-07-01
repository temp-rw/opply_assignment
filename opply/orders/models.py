from django.db import models

from base.db.constants import PRODUCT_NAME_MAX_LENGTH
from base.db.models import AbstractBaseModel
from iam.models import User
from products.models import Product


class Order(AbstractBaseModel):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)


class OrderedProduct(AbstractBaseModel):
    original_product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH)
    price = models.FloatField()
