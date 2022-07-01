from django.db import models

from base.db.constants import PRODUCT_NAME_MAX_LENGTH
from base.db.models import BaseEditableModel


class Product(BaseEditableModel):
    name = models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH)
    price = models.FloatField()
