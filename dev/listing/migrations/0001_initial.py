# Generated by Django 4.1.6 on 2023-02-07 18:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("realtors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zipcode", models.CharField(max_length=20)),
                ("description", models.TextField(blank=True)),
                ("price", models.IntegerField()),
                ("bedrooms", models.IntegerField()),
                ("bathrooms", models.DecimalField(decimal_places=1, max_digits=2)),
                ("garage", models.DecimalField(decimal_places=1, max_digits=5)),
                ("sqft", models.IntegerField()),
                ("lot_size", models.IntegerField()),
                ("photo_main", models.ImageField(upload_to="photo_main/%Y/%m/%d/")),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                (
                    "photo_3",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                (
                    "photo_4",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                (
                    "photo_5",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                (
                    "photo_6",
                    models.ImageField(blank=True, upload_to="photo_main/%Y/%m/%d/"),
                ),
                ("is_published", models.BooleanField(default=True)),
                (
                    "lsit_data",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "realtor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="realtors.realtor",
                    ),
                ),
            ],
        ),
    ]
