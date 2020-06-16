from django.contrib import admin
from apps.photos.models import Photo


@admin.register(Photo)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('image', 'position', 'car',)


