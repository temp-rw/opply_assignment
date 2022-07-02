from django.core.validators import MinValueValidator
from django.db import models

from base.db.constants import PRODUCT_NAME_MAX_LENGTH
from base.db.models import BaseEditableModel


class Product(BaseEditableModel):
    name = models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH)
    price = models.FloatField(validators=[MinValueValidator(0.0001)])
    product_stocks = models.ManyToManyField(
        to="orders.Stock", through="orders.ProductStock", through_fields=["product", "stock"]
    )

    def __str__(self):
        return f"{self.name}"
