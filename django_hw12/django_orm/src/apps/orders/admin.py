from django.contrib import admin
from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)

# @admin.register()
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# @admin.register(City)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('name',)

