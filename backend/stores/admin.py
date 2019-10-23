from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from stores.models import Category, Option, Store, BusinessRegistration

@admin.register(Store)
class StoreAdmin(OSMGeoAdmin):
    pass

admin.site.register(Category)
admin.site.register(Option)
# admin.site.register(Store)
admin.site.register(BusinessRegistration)