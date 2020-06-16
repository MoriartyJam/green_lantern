from django.db import models
from django.db.models.functions import Concat


class OrderQuerySet(models.QuerySet):
    def reserved(self):
        return self.filter(status='Reserved')

    def paid(self):
        return self.filter(status='Paid')

    def waiting_for_payment(self):
        return self.filter(status='Waiting for payment')

    def archived(self):
        return self.filter(status='Archived')

