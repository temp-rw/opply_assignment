# Generated by Django 4.0.5 on 2022-07-01 18:56

import base.db.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.CharField(default=base.db.utils.generate_uuid, editable=False, max_length=64, primary_key=True, serialize=False, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
