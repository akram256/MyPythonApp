from django.conf import settings
from django.urls import path, include

from metrics.views import MetricAttributesView, MetricAttributesRetrieveUpdateDestroy


urlpatterns = [
      path('metric/attribute', MetricAttributesView.as_view(), name='add-metric-attribute'),
      path('metric/attribute/<str:id>', MetricAttributesRetrieveUpdateDestroy.as_view(), name='update-delete'),
]