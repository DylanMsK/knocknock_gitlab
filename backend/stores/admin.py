from django.contrib import admin
from stores.models import Category, Option, Store, BusinessRegistration

admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Store)
admin.site.register(BusinessRegistration)