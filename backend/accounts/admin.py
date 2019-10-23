from django.contrib import admin
from accounts.models import Client, Partner

# Register your models here.
admin.site.register(Client)
admin.site.register(Partner)