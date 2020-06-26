from django.db import models
from django.contrib.auth.models import User
from django.db.models import Index, UniqueConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


# from src.config import settings


class Country(models.Model):
    CountryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    Code = models.PositiveIntegerField(default=2, editable=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Country')
        verbose_name_plural = _('Countrys')

    def __str__(self):
        return self.name


class City(models.Model):
    CityId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    CountryId = models.ForeignKey('dealers.Country', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('City')
        verbose_name_plural = _('Citys')

    def __str__(self):
        return self.name


class Dealer(User):
    DealerId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=32, unique=True)
    Email = models.EmailField(max_length=254)
    name = models.CharField(max_length=32, unique=True)
    CityId = models.ForeignKey('dealers.City', on_delete=models.CASCADE)


    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')

    @property
    def full_location(self):
        return '%s %s' % (City.name, Country.name)

    print(full_location)

    def __str__(self):
        return str(self.DealerId)
