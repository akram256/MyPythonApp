import os
import secrets
import re
import requests
import uuid 
import jwt
import json
import logging
from datetime import timedelta, datetime, time, date

from django.core.cache import cache
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.shortcuts import render


from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView

from .serializers import RegistrationSerializer,LoginSerializer
from accounts.models import User
from helpers import services

logger = logging.getLogger(__name__)


class RegistrationAPIView(generics.GenericAPIView):
    """Register new users."""
    serializer_class = RegistrationSerializer
    permission_class = (AllowAny,)

    def post(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(data=request.data)
        password = request.data.get('password')
        email = request.data.get('email')
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        user_name=request.data.get('user_name')
        phone_no=request.data.get('phone_no')
        email= str(email)
        email = email.lower()
        email_pattern = services.EMAIL_PATTERN
        password_pattern = services.PASSWORD_PATTERN
        # cache_key = email
        # if cache.get(cache_key):
        #     return Response({'message': f"Please visit your email {email} to complete registration", 'status': '00'}, status=status.HTTP_400_BAD_REQUEST)

        if not re.match(password_pattern,password):
            return Response({'message':'Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL',}, status=status.HTTP_400_BAD_REQUEST)
        
        if re.match(email_pattern,email):
            user = [i for i in users if i.email == email]
            if user:
                return Response({'message':'This email: {} , already belongs to a user on caesar reporting'.format(email),}, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.info('email looks good')
        else:
            return Response({'message':'Email: {} is not valid'.format(email),}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            user=User(email=email,password=password,first_name=first_name,last_name=last_name,
            is_active=True,
            phone_no=phone_no)
            user.set_password(password)
            print(user)
            print(password)
            user.save()


            # details = {'field':'auth','password':password,'email':email}
            logger.info(f'user {email} has been registered')
            return Response({'message': "Registration successful, Kindly check your email to activate your account", 'status': '00',
                    'token':user.token, 
                    'user_id':user.id,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                     "phone_no":user.phone_no}, 
                     status=status.HTTP_201_CREATED)
        return Response({'message': "Invalid credentials", 'status': '00'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset=User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)

        if serializer.is_valid(raise_exception=True):
            user = authenticate(email=email, password=password) 
            if user is None:
                users = User.objects.all()
                return Response ({'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if not user.is_active:
                    raise serializers.ValidationError(
                        'This account is not verified, Kindly check your email to verify account.'
                    )
                else:
                    logger.info('login successful for {}'.format(email))

            resp ={
                    'status':'00',
                    'id':user.id,
                    'token':user.token,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    # 'user_name':user.user_name,
                    'phone_no':user.phone_no,

                    'message':'user loggedin successfully'
                }
            return Response(resp, status=status.HTTP_200_OK)
                
        return Response({'message': "Invalid credentials", 'status': '00'}, status=status.HTTP_400_BAD_REQUEST)