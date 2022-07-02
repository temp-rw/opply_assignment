# Generated by Django 4.0.5 on 2022-07-01 20:36

import base.db.utils
import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.db.models.deletion
import iam.managers

from iam.migrations.commands.enable_ci_extension import enable_citext_extention


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        enable_citext_extention(),
        migrations.CreateModel(
            name="Role",
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
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("name", django.contrib.postgres.fields.citext.CICharField(max_length=256)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
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
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("username", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=50, verbose_name="first name")),
                ("last_name", models.CharField(max_length=50, verbose_name="last name")),
                ("email", django.contrib.postgres.fields.citext.CIEmailField(max_length=254, unique=True)),
                ("role", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="iam.role")),
            ],
            options={"abstract": False},
            managers=[("objects", iam.managers.UserManager())],
        ),
    ]
