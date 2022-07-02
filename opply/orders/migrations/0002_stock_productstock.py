# Generated by Django 4.0.5 on 2022-07-01 20:36

import base.db.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("products", "0001_initial"), ("orders", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "uuid",
                    models.CharField(
                        default=base.db.utils.generate_uuid,
                        editable=False,
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="uuid",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=250)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ProductStock",
            fields=[
                (
                    "uuid",
                    models.CharField(
                        default=base.db.utils.generate_uuid,
                        editable=False,
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="uuid",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("amount_in_stock", models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="products.product")),
                ("stock", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="orders.stock")),
            ],
            options={"abstract": False},
        ),
    ]
