from django.contrib import admin
from apps.newsletters.models import NewsLetter


@admin.register(NewsLetter)
class NewsLetter(admin.ModelAdmin):
    list_display = ('email',)