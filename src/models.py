from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    class Meta:
        db_table = 'user'


class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'

    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=100)
    issue_date = models.DateField(default=timezone.now)
    sale_date = models.DateField(default=timezone.now)
    payment_deadline = models.PositiveSmallIntegerField(default=14)
    payment_method = models.CharField(max_length=50, default="przelew")
    paid = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0))

    def __str__(self):
        return self.name
