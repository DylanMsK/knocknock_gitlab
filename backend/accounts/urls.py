from django.urls import path
from accounts.views import (
    ClientSignupAPI,
    PartnerSignupAPI,
    ClientLoginAPI,
    PartnerLoginAPI
)


urlpatterns = [
    path('client/signup/', ClientSignupAPI.as_view(), name='client_signup'),
    path('client/login/', ClientLoginAPI.as_view(), name='client_login'),
    path('partner/signup/', PartnerSignupAPI.as_view(), name='partner_signup'),
    path('partner/login/', PartnerLoginAPI.as_view(), name='partner_login'),
]

