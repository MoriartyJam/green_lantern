from django.contrib import admin
from apps.orders.models import Order


@admin.register(Order)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('Status',)
