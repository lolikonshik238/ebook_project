# Generated by Django 5.1.1 on 2024-11-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0011_remove_cartitem_cart_remove_cartitem_product_basket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default='Нет данных'),
        ),
    ]
