# Generated by Django 5.1.7 on 2025-04-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_small_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_1920x640',
            field=models.ImageField(default='', upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_330x220',
            field=models.ImageField(default='', upload_to='blog'),
        ),
    ]
