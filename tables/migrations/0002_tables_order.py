# Generated by Django 4.1.4 on 2022-12-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_recipt_order_orders_order'),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tables',
            name='order',
            field=models.ManyToManyField(to='orders.orders'),
        ),
    ]