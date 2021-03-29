from django.db import models
from helpers.models import BaseAbstractModel
from datetime import datetime, timedelta
from django.conf import settings
from decimal import Decimal



class FrameWorks(BaseAbstractModel):
    """This is a FrameWorks model """
   
    name = models.CharField(max_length=15, unique=True,blank=True, null=True)
    metricattribute = models.ForeignKey('metrics.MetricAttributes', on_delete=models.CASCADE)
    founded  = models.CharField(max_length=255, blank=True, null=True)
    support = models.CharField(max_length=255, blank=True, null=True)
    adoption = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    overview = models.CharField(max_length=255, blank=True, null=True)
    implementation = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    DueDate = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name
