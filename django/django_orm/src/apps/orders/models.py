from django.db import models


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    models.ManyToManyField(to='cars.Car', related_name='orders')
    Status = models.CharField(max_length=64)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    Email = models.EmailField(max_length=70, blank=True)
    Phone = models.CharField(max_length=64, default='0-000-000-00')

    def __str__(self):
        return self.name
