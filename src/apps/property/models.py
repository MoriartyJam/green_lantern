from django.db import models


class Property(models.Model):
    PropertyID = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=64)
    Name = models.CharField(max_length=64)


class CarProperty(models.Model):
    CarPropertyID = models.AutoField(primary_key=True)
    PropertyID = models.ForeignKey('property.Property', on_delete=models.CASCADE)
    CarID = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
