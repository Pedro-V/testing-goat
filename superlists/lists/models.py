from django.db import models

# ORM
class Item(models.Model):
    text = models.TextField(default='')
