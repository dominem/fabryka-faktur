from django.contrib.admin import AdminSite, ModelAdmin

from .models import Invoice, Company, Address, BankAccount


class FabrykaFakturAdminSite(AdminSite):
    site_title = 'Fabryka Faktur'
    site_header = site_title
    index_title = site_title


site = FabrykaFakturAdminSite()


class InvoiceAdmin(ModelAdmin):
    list_display = ('id', 'name', 'issue_date', 'sale_date')


class CompanyAdmin(ModelAdmin):
    list_display = ('id', 'name', 'tax_id')


class AddressAdmin(ModelAdmin):
    list_display = ('id', 'country', 'city', 'zip_code', 'street', 'street_number')


class BankAccountAdmin(ModelAdmin):
    list_display = ('id', 'bank_name', 'bank_account_number')


site.register(Invoice, InvoiceAdmin)
site.register(Company, CompanyAdmin)
site.register(Address, AddressAdmin)
site.register(BankAccount, BankAccountAdmin)
