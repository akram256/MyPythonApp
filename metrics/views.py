import logging

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string


from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView,ListAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny,IsAuthenticated

from .models import MetricAttributes
from .serializers import MetricAttributesSerializer
from accounts.models import User
from django.contrib.contenttypes.models import ContentType



logger = logging.getLogger(__name__)

class MetricAttributesView(ListAPIView):
    serializer_class=MetricAttributesSerializer
    permission_classes=(AllowAny,)
    queryset=MetricAttributes.objects.all()

    def post(self, request):
       
        post_data = {"name":request.data["name"],"metric_type":request.data["metric_type"]}
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Metric Attribute has been  successfully added"},
                        status=status.HTTP_201_CREATED)


class MetricAttributesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes =(AllowAny,)
    serializer_class = MetricAttributesSerializer
    lookup_field = 'id'
    queryset=MetricAttributes.objects.all()
    

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), id=self.kwargs.get('id'))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message':'Successfully updated',
            'data':serializer.data},status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Metric Attribute has been successfully deleted"},
                        status=status.HTTP_200_OK)