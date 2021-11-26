from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=222)
    body = models.TextField()
    cost = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
