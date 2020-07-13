from django.contrib.admin import AdminSite


class FabrykaFakturAdminSite(AdminSite):
    site_title = 'Fabryka Faktur'
    site_header = site_title
    index_title = site_title


site = FabrykaFakturAdminSite()
