from django.db import models

class Banks(models.Model):
    name = models.CharField(max_length=50)

class Branches(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id= models.IntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state= models.CharField(max_length=26)
    