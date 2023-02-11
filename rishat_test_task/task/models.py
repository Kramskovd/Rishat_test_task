from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Item(models.Model):
    item = models.CharField(max_length=50, verbose_name='Item')
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(verbose_name='Price')

    def __str__(self):
        return self.item


class Order(models.Model):
    item = models.ManyToManyField(Item)

    def __str__(self):
        return "Order " + str(self.id)


class Discount(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)


class Tax(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tax = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)