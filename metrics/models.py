from django.db import models
from helpers.models import BaseAbstractModel
from django.conf import settings
from decimal import Decimal
from frameworks.models import FrameWorks



class MetricAttributes(BaseAbstractModel):
    """This is a Metric Attributes model """
    name = models.CharField(max_length=15, unique=True,blank=True, null=True)
    metric_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Metrics(BaseAbstractModel):
    frameworkid = models.ForeignKey(FrameWorks, on_delete=models.CASCADE, null= True)
    jsonifiedmetricvalues = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # reviewerid = models.ForeignKey(GameOperator, on_delete=models.CASCADE, null= True)
    owner = models.ForeignKey(GameOperator, on_delete=models.CASCADE, null= True)
    isOwnerAssigned = models.BooleanField(default=False)
    hasOwnerComfirmed = models.BooleanField(default=False)
    isReviewerAssigned = models.BooleanField(default=False)
    HasReviewerConfrimed = models.BooleanField(default=False)



