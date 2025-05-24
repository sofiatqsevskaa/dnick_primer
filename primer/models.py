from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bakers/', null=True, blank=True)

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="cakes/", null=True, blank=True)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, related_name="cakes", blank=True, null=True)

