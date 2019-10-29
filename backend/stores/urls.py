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
from menus.views import (
    RetrieveCreateMenuAPI,
    RetrieveUpdateDeleteMenuAPI
)

urlpatterns = [
    path('', StoreListAPI.as_view(), name='store_list'),
    path('<int:store_id>/', StoreDetailAPI.as_view(), name='store_detail'),

    path('<int:store_id>/reviews/', RetrieveCreateClientReviewAPI.as_view(), name='create_client_review'),
    path('<int:store_id>/reviews/<int:review_id>/', DeleteClientReivewAPI.as_view(), name='delete_client_review'),
    path('<int:store_id>/reviews/<int:review_id>/feedback/', RetrieveCreatePartnerFeedbackAPI.as_view(), name='create_partner_feedback'),
    path('<int:store_id>/reviews/<int:review_id>/feedback/<int:feedback_id>/', DeletePartnerFeedbackAPI.as_view(), name='delete_partner_feedback'),

    path('<int:store_id>/menus/', RetrieveCreateMenuAPI.as_view(), name='create_menu'),
    path('<int:store_id>/menus/<int:menu_id>/', RetrieveUpdateDeleteMenuAPI.as_view(), name='edit_menu'),

    path('search/', SearchStoreAPI.as_view(), name='search_store'),
]