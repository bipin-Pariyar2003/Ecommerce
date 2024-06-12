# Generated by Django 5.0.6 on 2024-06-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0014_cartitem_user_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered')], default='pending', max_length=20),
        ),
    ]
