from django.db import models
from helpers.models import BaseAbstractModel
from datetime import datetime, timedelta
from django.conf import settings
from decimal import Decimal



class Company(BaseAbstractModel):
    """This is a company model """

    name = models.CharField(max_length=15, unique=True,blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, unique=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    LastRenewalDate = models.DateTimeField()
    NextChargeDate = models.DateTimeField()


    def __str__(self):
        return self.name