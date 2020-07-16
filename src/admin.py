from django.contrib.admin import AdminSite, ModelAdmin

from .models import Invoice


class FabrykaFakturAdminSite(AdminSite):
    site_title = 'Fabryka Faktur'
    site_header = site_title
    index_title = site_title


site = FabrykaFakturAdminSite()


class InvoiceAdmin(ModelAdmin):
    list_display = ('id', 'name', 'issue_date', 'sale_date')


site.register(Invoice, InvoiceAdmin)
