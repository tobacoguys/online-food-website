# Generated by Django 4.2 on 2024-02-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_cartorder_coupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='saved',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
    ]
