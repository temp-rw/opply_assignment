# Generated by Django 4.0.5 on 2022-07-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0004_alter_productstock_amount_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_products',
            field=models.ManyToManyField(through='orders.ProductStock', to='products.product'),
        ),
    ]
