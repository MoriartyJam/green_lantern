from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _

from apps.cars.managers import CarManager, CarQuerySet
from apps.dealers.models import Dealer
from common.models import BaseDateAuditModel


class Color(models.Model):
    ColorId = models.AutoField(primary_key=True)
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
    BrandId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    Logo = models.ImageField(null=True, blank=False)

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
    ModelId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    BrandId = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

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
    # views = models.PositiveIntegerField(default=0, editable=False)
    # slug = models.SlugField(max_length=75)
    # number = models.CharField(max_length=16, unique=True)
    # status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    # # dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE, related_name='cars')
    #
    # model = models.ForeignKey(to='CarModel', on_delete=models.NULL, null=True, blank=False)
    # extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))
    carId = models.AutoField(primary_key=True)
    ColorId = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='cars', null=True, blank=False)
    DealerID = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealers', null=True, blank=False)
    ModelId = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, related_name='cars', null=True, blank=False)
    models.ManyToManyField(to='dealers.Dealer', related_name='cars')
    EngineType = models.CharField(max_length=16, null=True)
    PopulationType = models.CharField(max_length=20, null=True)
    Price = models.PositiveIntegerField(default=0, editable=True)
    FuelType = models.CharField(max_length=10, null=True)
    Status = models.CharField(max_length=10, null=True)
    Doors = models.PositiveIntegerField(default=2, editable=True)
    Capacity = models.CharField(max_length=10, null=True)
    GearCase = models.CharField(max_length=10, null=True)
    Number = models.CharField(max_length=16, unique=True)
    Slug = models.SlugField(max_length=75)
    SittingPlace = models.PositiveIntegerField(default=2)
    FirstRegistrationDate = models.DateField(auto_now=False, auto_now_add=True)
    EnginePower = models.PositiveIntegerField(default=0, editable=True)

    # other fields ...
    #

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.Number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.Status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.Brand} {self.carId or ""}'  # do not show None

    def __str__(self):
        return str(self.carId)


    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['Status', ])
        ]
