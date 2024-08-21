from django.db import models

class Banner(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    




