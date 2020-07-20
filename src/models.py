from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from pycountry import countries


COUNTRIES = [c.name for c in countries]
COUNTRIES = zip(COUNTRIES, COUNTRIES)
POLAND = countries.get(alpha_2='PL').name


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


class Company(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    name = models.CharField(max_length=100, verbose_name=_('Name'))
    tax_id = models.CharField(max_length=100, verbose_name=_('Tax ID'))
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, verbose_name=_('Address'))
    bank_account = models.ForeignKey('BankAccount', on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name=_('Bank account'))

    def __str__(self):
        return self.name


class Address(models.Model):
    class Meta:
        db_table = 'address'
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    country = models.CharField(max_length=50, choices=COUNTRIES, default=POLAND, verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    zip_code = models.CharField(max_length=100, verbose_name=_('ZIP Code'))
    street = models.CharField(max_length=100, verbose_name=_('Street'))
    street_number = models.CharField(max_length=100, verbose_name=_('Street number'))

    def __str__(self):
        return f'{self.city} {self.zip_code}, {self.street} {self.street_number}'


class BankAccount(models.Model):
    class Meta:
        db_table = 'bank_account'
        verbose_name = _('Bank Account')
        verbose_name_plural = _('Bank Accounts')

    bank_name = models.CharField(max_length=100, default='', blank=True, verbose_name=_('Bank name'))
    bank_account_number = models.CharField(max_length=32, verbose_name=_('Bank account number'))

    def __str__(self):
        return f'{self.bank_name}, {self.bank_account_number}'
