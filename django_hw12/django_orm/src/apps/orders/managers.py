from django.db import models
from django.db.models import Orders

from src.apps.orders.models import Order


class OrderQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

    def reserved(self):
        return self.filter(status='reserved')

    def paid(self):
        return self.filter(status='paid')

    def waiting(self):
        return self.filter(status='Waiting for payment')

    def filter(self, *args, **kwargs):
        Orders.objects.filter(status='paid')


class OrdersStatus(models.QuerySet):
    def filter(self):
        Orders.objects.filter(status='paid')


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('car')
