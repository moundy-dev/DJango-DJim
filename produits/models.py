from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()


# Create your models here.
