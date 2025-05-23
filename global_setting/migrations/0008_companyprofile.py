# Generated by Django 5.1.7 on 2025-05-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("global_setting", "0007_footertext"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyProfile",
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
                (
                    "company_alias",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "company_logo_69x42",
                    models.ImageField(
                        blank=True, null=True, upload_to="global_setting"
                    ),
                ),
                (
                    "company_logo_138x84",
                    models.ImageField(
                        blank=True, null=True, upload_to="global_setting"
                    ),
                ),
                (
                    "favicon_16x16",
                    models.ImageField(
                        blank=True, null=True, upload_to="global_setting"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
