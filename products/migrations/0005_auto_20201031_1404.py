# Generated by Django 3.1.2 on 2020-10-31 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_nutritions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritions',
            name='drink_id',
        ),
        migrations.AddField(
            model_name='nutritions',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
