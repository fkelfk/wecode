from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        abstract = True

class Owner(CommonInfo):
    email = models.CharField(max_length=300)

    class Meta:
        db_table = 'Owners'

    def __str__(self):
        return self.name

class Dog(CommonInfo):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Dogs'

    def __str__(self):
        return self.name
