from django.urls import path
from partners.views import (
    PartnerStoreListAPI,
    PartnerStoreDetailAPI
)

urlpatterns = [
    path('partner/', PartnerStoreListAPI.as_view(), name='manage_store_list'), 
    path('partner/<int:pk>/', PartnerStoreDetailAPI.as_view(), name='manage_store_detail'), 
]