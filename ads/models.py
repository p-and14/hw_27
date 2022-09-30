from django.db import models


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=25)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
