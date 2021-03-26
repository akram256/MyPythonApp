import logging
from rest_framework import serializers
from .models import MetricAttributes


logger = logging.getLogger(__name__)


class MetricAttributesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MetricAttributes
        fields = (
            'id',
            'name',
            'metric_type'

        )