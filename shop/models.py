import email
from email.policy import default
from itertools import product
from re import T
from statistics import mode
from unicodedata import category
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image =models.ImageField(upload_to='shop/images', default="")

    def __str__(self) -> str:
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_jason = models.CharField(max_length=2000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.update_desc[0:7] + "..."