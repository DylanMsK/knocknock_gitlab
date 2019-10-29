from django.urls import path
from stores.views import (
    StoreListAPI,
    StoreDetailAPI,
    CreateStoreReviewAPI,
    DeleteStoreReivewAPI,
    SearchStoreAPI
)

urlpatterns = [
    path('', StoreListAPI.as_view(), name='store_list'),
    path('<int:pk>/', StoreDetailAPI.as_view(), name='store_detail'),
    path('<int:store_id>/reviews/', CreateStoreReviewAPI.as_view(), name='create_store_review'),
    path('<int:store_id>/reviews/<int:review_id>/', DeleteStoreReivewAPI.as_view(), name='delete_store_review'),
    path('search/', SearchStoreAPI.as_view(), name='search_store'),
]