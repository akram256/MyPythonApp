import logging
from rest_framework import serializers
from .models import Company


logger = logging.getLogger(__name__)


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'phone_number',
            'email',
            'industry',
            'sector',
            'status',
            )
        read_only_fields = ('id',)
