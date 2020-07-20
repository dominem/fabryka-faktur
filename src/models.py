from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    class Meta:
        db_table = 'user'


class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')

    name = models.CharField(max_length=50, verbose_name=_('Name'))
    filename = models.CharField(max_length=100, verbose_name=_('Filename'))
    issue_date = models.DateField(default=timezone.now, verbose_name=_('Issue date'))
    sale_date = models.DateField(default=timezone.now, verbose_name=_('Sale date'))
    payment_deadline = models.PositiveSmallIntegerField(default=14, verbose_name=_('Payment deadline'))
    payment_method = models.CharField(max_length=50, default="przelew", verbose_name=_('Payment method'))
    paid = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0), verbose_name=_('Paid'))

    def __str__(self):
        return self.name
