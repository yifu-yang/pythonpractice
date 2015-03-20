from django.db import models

# Create your models here.

class message(models.Model):
    name=models. CharField(max_length=20)
    message = models.CharField(max_length=200)
    time= models.DateTimeField()