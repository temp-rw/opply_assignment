from django.db import models

from base.db.utils import generate_uuid


class AbstractBaseModel(models.Model):
    uuid = models.CharField(
        primary_key=True,
        default=generate_uuid,
        editable=False,
        verbose_name='uuid',
        max_length=64
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
