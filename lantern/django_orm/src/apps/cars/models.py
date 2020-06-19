from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _

from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Picture(models.Model):
    PictureID = models.AutoField(primary_key=True)
    URL = models.URLField(max_length=200)
    Position = models.CharField(max_length=64)
    Metadata = models.CharField(max_length=64)


class Color(models.Model):
    ColorID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    ModelID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    objects = CarManager.from_queryset(CarQuerySet)()
    CarID = models.AutoField(primary_key=True)
    ColorID = models.ForeignKey('cars.color', on_delete=models.CASCADE)
    DealerID = models.ForeignKey('dealers.dealer', on_delete=models.CASCADE)
    ModelID = models.ForeignKey('cars.CarModel', on_delete=models.CASCADE)
    EngineType = models.TextField(blank=True)
    PopulationType = models.TextField(blank=True)
    Price = models.FloatField(null=True, blank=True)
    FuelType = models.TextField(blank=True)
    Doors = models.IntegerField(null=True, blank=True)
    Capacity = models.IntegerField(null=True, blank=True)
    GearCase = models.CharField(max_length=16, null=False)
    Sitting_Place = models.IntegerField(null=True, blank=True)
    FirstRegistrationDate = models.DateField(null=True, blank=True)
    EnginePower = models.FloatField(null=True, blank=True)
    other = models.CharField(max_length=16, null=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    number = models.CharField(max_length=16, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['status', ])
        ]
