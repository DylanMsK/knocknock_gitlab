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
    Review
)

@admin.register(Store)
class StoreAdmin(OSMGeoAdmin):
    pass

admin.site.register(Category)
admin.site.register(Option)
admin.site.register(BusinessHour)
admin.site.register(PublicHoliday)
admin.site.register(HolidayHour)
admin.site.register(Dayoff)
admin.site.register(Review)
