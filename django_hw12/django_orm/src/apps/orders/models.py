from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    STATUS_RESERVED = "reserved"
    STATUS_PAID = "paid"
    STATUS_WAITING_FOR_PAYMENT = "waiting for payment"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = (
        (STATUS_RESERVED, "Reserved"),
        (STATUS_PAID, "Paid"),
        (STATUS_WAITING_FOR_PAYMENT, "Waiting for payment"),
        (STATUS_ARCHIVED, "Archived"),
    )

    # models.ManyToManyField(to='cars.Car', related_name='orders')

    status = models.CharField(
        max_length=19, choices=STATUS_CHOICES, default=STATUS_RESERVED, blank=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=255)

    class Meta:
        indexes = [Index(fields=("status",))]

        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    @property
    def full_info(self):
        return f'{self.first_name} {self.last_name} {self.car} : {self.status}'

    def __str__(self):
        return self.status



