# Generated by Django 5.1.7 on 2025-05-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_alter_productimage_product_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productcategory",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
