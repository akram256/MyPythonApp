from django.conf import settings
from django.urls import path, include

from frameworks.views import FrameWorksView


urlpatterns = [
      path('framework', FrameWorksView.as_view(), name='add-framework'),
]