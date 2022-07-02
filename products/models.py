from django.db import models

# Create your models here

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

    def __str__(self):
        return self.korean_name

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    drink = models.ForeignKey('drink', null=True, on_delete=models.CASCADE)
    size = models.ForeignKey('size', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.name


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'image'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    drinks = models.ManyToManyField('Drink', related_name='allergy')

    class Meta:
        db_table = 'allergy'

    def __str__(self):
        return self.name



