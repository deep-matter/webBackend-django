from django.db import models
from datetime import datetime as date

class Realtor(models.Model):
    """
    ID is automatically generated from foreign key
    """
    name = models.CharField(max_length=20)
    phone = models.ImageField(upload_to="photo_main/%Y/%m/d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=date.now,blank=True)
    def __str__(self):
        return self.name