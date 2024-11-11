from django.db import models
import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name       

class Customer(models.Model):
    ho = models.CharField(max_length=10)
    ten = models.CharField(max_length=50)
    dienthoai = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return f'{self.ho} {self.ten}'  

class Product(models.Model):
    name = models.CharField(max_length=250,null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/product/")

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=12, default="", blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Order of {self.quantity} {self.product.name}(s) by {self.customer}'
