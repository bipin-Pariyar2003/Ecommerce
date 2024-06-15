# Generated by Django 5.0.6 on 2024-06-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0023_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiver_address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='receiver_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='receiver_phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
