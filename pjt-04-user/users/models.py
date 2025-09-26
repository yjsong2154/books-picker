from django.db import models

class MyBooks(models.Model) :
    title = models.CharField(max_length=200)
    status = models.BooleanField(null = True)
    rating = models.FloatField(null = True)
    review = models.TextField(blank = True)
    
