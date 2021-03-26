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

from django.contrib.contenttypes.models import ContentType

from .models import FrameWorks
from .serializers import FrameWorksSerializer

logger = logging.getLogger(__name__)

class FrameWorksView(ListAPIView):
    serializer_class=FrameWorksSerializer
    permission_classes=(AllowAny,)
    queryset=FrameWorks.objects.all()

    def post(self, request):
       
        post_data = {"name":request.data["name"],"founded":request.data["founded"],
                     "adoption":request.data["adoption"],
                     "frequency":request.data["frequency"],
                     "website":request.data["website"],
                     "overview":request.data["overview"], 
                     "implementation":request.data["implementation"],
                     "reference":request.data["reference"],
                     "DueDate":request.data["DueDate"], 
                    #  "metricattribute":request.data["metricattribute"]
                     }
                    
                     
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Framework has been  successfully added"},
                        status=status.HTTP_201_CREATED)