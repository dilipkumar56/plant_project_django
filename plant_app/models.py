from django.db import models

# Create your models here.


class Products(models.Model):
    tittle = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    gmail = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=1000)
    total = models.CharField(max_length=100)
