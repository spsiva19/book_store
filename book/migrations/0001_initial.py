# Generated by Django 4.2.11 on 2024-04-22 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(max_length=255)),
                ('bname', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('pub_year', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email_id', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='book_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(max_length=255)),
                ('bname', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('bc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book_details')),
                ('uc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.user_reg')),
            ],
        ),
    ]