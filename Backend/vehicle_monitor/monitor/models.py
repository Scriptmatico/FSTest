from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
