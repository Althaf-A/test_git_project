from django.db import models

# Create your models here.

class new(models.Model):
    name=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)

    # selection 
    select = models.EmailField(max_length=30, default='')

