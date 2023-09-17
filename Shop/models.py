from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    quan = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
