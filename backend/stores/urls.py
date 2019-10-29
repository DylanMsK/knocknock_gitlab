from django.urls import path
from stores.views import (
    StoreListAPI,
    StoreDetailAPI,
    RetrieveCreateClientReviewAPI,
    DeleteClientReivewAPI,
    RetrieveCreatePartnerFeedbackAPI,
    DeletePartnerFeedbackAPI,
    SearchStoreAPI
)

urlpatterns = [
    path('', StoreListAPI.as_view(), name='store_list'),
    path('<int:pk>/', StoreDetailAPI.as_view(), name='store_detail'),
    path('<int:store_id>/reviews/', RetrieveCreateClientReviewAPI.as_view(), name='create_client_review'),
    path('<int:store_id>/reviews/<int:review_id>/', DeleteClientReivewAPI.as_view(), name='delete_client_review'),
    path('<int:store_id>/reviews/<int:review_id>/feedback/', RetrieveCreatePartnerFeedbackAPI.as_view(), name='create_partner_feedback'),
    path('<int:store_id>/reviews/<int:review_id>/feedback/<int:feedback_id>/', DeletePartnerFeedbackAPI.as_view(), name='delete_partner_feedback'),
    path('search/', SearchStoreAPI.as_view(), name='search_store'),
]