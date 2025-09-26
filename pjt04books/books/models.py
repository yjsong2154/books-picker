from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=10)
    stars = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
