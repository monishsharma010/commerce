# Generated by Django 4.2.5 on 2023-09-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_alter_listings_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="price",
            field=models.FloatField(blank=True, max_length=10),
        ),
    ]
