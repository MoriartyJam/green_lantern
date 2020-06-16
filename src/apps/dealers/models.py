from django.db import models
from django.contrib.auth.models import User


class Dealer(User):
    DealerID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=64)
    Email = models.EmailField(max_length=70, blank=True)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    CityID = models.ForeignKey('dealers.City', on_delete=models.CASCADE)

    @property
    def full_contact(self):
        # "Returns the person's full contact information."
        return '%s  %s %s' % (self.FirstName, self.LastName, self.Email)


class City(models.Model):
    CityID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=64)
    CountryID = models.ForeignKey('dealers.Country', on_delete=models.CASCADE)


class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=64)
    Code = models.IntegerField(null=True, blank=True)
