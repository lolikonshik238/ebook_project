# Generated by Django 5.1.1 on 2024-11-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0009_cart_cartitem_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(related_name='carts', to='startit_app.book'),
        ),
    ]