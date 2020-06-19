from django.contrib import admin
from apps.dealers.models import Dealer, City, Country


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('Name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
