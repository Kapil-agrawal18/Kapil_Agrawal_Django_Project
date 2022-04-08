from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid

cat = {
    ('Furnishing', 'Furnishing'),
    ('Lighting', 'Lighting'),
    ('Walls & Floor', 'Walls & Floor'),
}

sub_cat = {
    ('Furniture', 'Furniture'),
    ('Lighting', 'Lighting'),
    ('Carpet', 'Carpet'),
    ('Kitchen', 'Kitchen'),
    ('Bath', 'Bath'),
    ('Wellness', 'Wellness'),
}

sub_sub_cat = {
    ('alpha', 'alpha'),
    ('beta', 'beta'),
    ('Gama', 'Gama'),
    ('delta', 'delta'),
}


# Create your models here.
class Product(models.Model):
    # product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=cat)
    subcategory = models.CharField(
        max_length=30, choices=sub_cat)
    sub_sub_category = models.CharField(
        max_length=30, choices=sub_sub_cat)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=2000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="static")

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
