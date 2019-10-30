from django.contrib import admin
from clients.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'content', 'created_at')
    list_display = ('id', 'store',)