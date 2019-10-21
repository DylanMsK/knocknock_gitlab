from django.contrib import admin
from stores.models import Category, Option, Store

# Register your models here.
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Store)