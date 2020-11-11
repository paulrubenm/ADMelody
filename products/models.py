from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=120)
