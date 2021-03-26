from django.conf import settings
from django.urls import path, include

from companies.views import CompanyView


urlpatterns = [
      path('company', CompanyView.as_view(), name='add-company'),
]