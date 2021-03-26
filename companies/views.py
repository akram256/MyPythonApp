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

from .models import Company
from .serializers import CompanySerializer
from accounts.models import User
from django.contrib.contenttypes.models import ContentType



logger = logging.getLogger(__name__)

class CompanyView(ListAPIView):
    serializer_class=CompanySerializer
    permission_classes=(AllowAny,)
    queryset=Company.objects.all()

    def post(self, request):
       
        post_data = {"name":request.data["name"],"phone_number":request.data["phone_number"],
                     "email":request.data["email"],"industry":request.data["industry"],"sector":request.data["sector"], "status":True }
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Company has been  successfully added"},
                        status=status.HTTP_201_CREATED)