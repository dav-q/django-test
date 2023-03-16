from django.db import models

# Create your models here.

# Create your models here.
class Client(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)