# Generated by Django 5.0.6 on 2024-06-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0028_alter_product_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(),
        ),
    ]
