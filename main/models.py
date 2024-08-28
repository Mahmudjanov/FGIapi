from django.db import models


class Banner(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)



class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    


class Form(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()



class Contact(models.Model):
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)