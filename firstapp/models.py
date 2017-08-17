from django.db import models

class Item(models.Model):
  
    first_name=models.CharField(max_length=100, null=True)
    last_name=models.CharField(max_length=100, null=True)
    home=models.CharField(max_length=100, null=True)
