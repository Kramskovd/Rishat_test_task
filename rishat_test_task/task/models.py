from django.db import models

# Create your models here.


class Item(models.Model):
    item = models.CharField(max_length=50, verbose_name='Item')
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(verbose_name='Price')


class Order(models.Model):
    order_number = models.IntegerField(verbose_name='Order number')
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='Item ID')
