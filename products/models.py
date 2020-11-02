from django.db import models

# Create your models here.


class Menu(models.Model):
		name = models.CharField(max_length=20)


class Category(models.Model):
		name = models.CharField(max_length=20)
		menu = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Product(models.Model):
		name  = models.CharField(max_length=100)
		english_name = models.CharField(max_length=100, default="")
		description = models.CharField(max_length=100, default="")
		category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Nutritions(models.Model):
        one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        sugars_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        protein_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        product = models.ForeignKey('Product', on_delete=models.CASCADE, default="")

class Images(models.Model):
        image_url = models.CharField(max_length=1000)
        product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Sizes(models.Model):
        name = models.CharField(max_length=20, blank=True, null=True)
        size_ml = models.CharField(max_length=20, blank=True, null=True)
        size_fluid_ounce = models.CharField(max_length=20, blank=True, null=True) 
        nutrition = models.ForeignKey('Nutritions',on_delete=models.CASCADE)

class Allergy(models.Model):
        name = models.CharField(max_length=20, blank=True, null=True)

class Allergy_Product(models.Model):
        product = models.ForeignKey('Product', on_delete=models.CASCADE)
        allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
