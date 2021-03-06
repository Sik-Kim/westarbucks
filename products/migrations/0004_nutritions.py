# Generated by Django 3.1.2 on 2020-10-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201031_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kca', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sodium_mg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('saturated_fat_g', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sugars_g', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('protein_g', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('caffeine_mg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('drink_id', models.IntegerField()),
            ],
        ),
    ]
