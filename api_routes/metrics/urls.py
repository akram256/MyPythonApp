from django.conf import settings
from django.urls import path, include

from metrics.views import MetricAttributesView


urlpatterns = [
      path('metric/attribute', MetricAttributesView.as_view(), name='add-metric-attribute'),
]