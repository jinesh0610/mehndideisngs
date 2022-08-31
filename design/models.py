from tkinter import Widget
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=55)
    phone = models.IntegerField()
    note = models.TextField()
