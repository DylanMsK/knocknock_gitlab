from django.urls import path
from partners.views import (
    PartnerStoreListAPI,
    PartnerStoreDetailAPI,
    BusinessRegistrationAPI
)

urlpatterns = [
    path('stores/', PartnerStoreListAPI.as_view(), name='manage_store_list'),
    path('stores/<int:store_id>/', PartnerStoreDetailAPI.as_view(), name='manage_store_detail'),
    path('regist/', BusinessRegistrationAPI.as_view())
]