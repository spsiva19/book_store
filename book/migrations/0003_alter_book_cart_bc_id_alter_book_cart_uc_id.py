# Generated by Django 4.2.11 on 2024-04-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_cart_bc_id_alter_book_cart_uc_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_cart',
            name='bc_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_cart',
            name='uc_id',
            field=models.IntegerField(),
        ),
    ]
