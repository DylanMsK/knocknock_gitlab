from django.urls import path
from knox import views as knox_views
from accounts.views.client_views import (
    ClientSignupAPI,
    ClientLoginAPI,
    ClientUserAPI
)
from accounts.views.partner_views import (
    PartnerSignupAPI,
    PartnerLoginAPI,
    PartnerUserAPI
)


urlpatterns = [
    path('logout/', knox_views.LogoutView.as_view(), name="logout"),

    path('client/signup/', ClientSignupAPI.as_view(), name='client_signup'),
    path('client/login/', ClientLoginAPI.as_view(), name='client_login'),
    path('client/auth/', ClientUserAPI.as_view()),

    path('partner/signup/', PartnerSignupAPI.as_view(), name='partner_signup'),
    path('partner/login/', PartnerLoginAPI.as_view(), name='partner_login'),
    path('partner/auth/', PartnerUserAPI.as_view())
]

