from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from apps.cars.models import Color, CarModel, CarBrand

from apps.cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('carId',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', '_image')

    def _image(self, obj):
        if obj.Logo:
            return mark_safe(f'<img src="{obj.Logo.url}" style="height: 50px">')
        return '----'
