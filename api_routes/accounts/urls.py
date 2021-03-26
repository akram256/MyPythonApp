from django.conf import settings
from django.urls import path, include

from accounts.views import RegistrationAPIView, LoginAPIView


urlpatterns = [
    path('login', LoginAPIView.as_view(), name='user-login'),
    path('register', RegistrationAPIView.as_view(), name='user-registration'),
]