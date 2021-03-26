import logging
from rest_framework import serializers
from .models import FrameWorks


logger = logging.getLogger(__name__)


class FrameWorksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FrameWorks
        fields = (
            'id',
            'name',
            'metricattribute',
            'founded',
            'adoption',
            'frequency',
            'website',
            'overview',
            'implementation',
            'reference',
            'DueDate',
            )
        read_only_fields = ('id',)
