# Generated by Django 5.0.1 on 2024-01-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.TextField(editable=False, unique=True),
        ),
    ]
