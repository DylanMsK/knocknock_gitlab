from django.urls import path
from stores.views import (
    StoreListAPI,
    StoreDetailAPI,
    SearchStoreAPI
)

urlpatterns = [
    path('', StoreListAPI.as_view(), name='store_list'),
    path('<int:pk>/', StoreDetailAPI.as_view(), name='store_detail'),
    path('search/', SearchStoreAPI.as_view(), name='search_store'),
]