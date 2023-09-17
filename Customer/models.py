from django.db import models
from django.contrib.auth.models import User
from Shop.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

Status=(
    ('Approved','Approved'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
)
class Order(models.Model):
    Address=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    price=models.IntegerField(max_length=200)
    Status = models.CharField(max_length=50, null=True, choices=Status, default='Pending')



