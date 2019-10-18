from django.urls import path
from stores.views import StoreListAPI, StoreDetailAPI

urlpatterns = [
    path('', StoreListAPI.as_view(), name='store_list'),
    path('<int:pk>/', StoreDetailAPI.as_view(), name='store_detail')
]