from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from stores.models import (
    Category,
    Option,
    Store,
    BusinessHour,
    PublicHoliday,
    HolidayHour,
    Dayoff,
    ClientReview,
    PartnerFeedback
)

@admin.register(Store)
class StoreAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'category', 'lon', 'lat', 'road_addr',)
    list_display_links = ('id', 'name',)
    list_filter = ('category', 'common_addr',)
    search_fields = ('name', 'road_addr', 'common_addr', 'addr',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_category', 'sub_category',)
    list_display_links = ('id', 'main_category', 'sub_category',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'content', 'created_at')
    list_display = ('id', 'store',)


@admin.register(PartnerFeedback)
class PartnerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'content', 'created_at',)
    list_display_links = ('id', 'store',)


admin.site.register(BusinessHour)
admin.site.register(PublicHoliday)
admin.site.register(HolidayHour)
admin.site.register(Dayoff)
