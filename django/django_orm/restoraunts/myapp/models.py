from django.db import models


class Cities(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Dishes(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    calorific = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dishes'


class Menu(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Restaurant(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Staff(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

