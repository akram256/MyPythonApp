from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from helpers.models import BaseAbstractModel
from .manager import UserManager
import uuid
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

class User(AbstractBaseUser, PermissionsMixin, BaseAbstractModel):
    """This is a user model """
    # ROLES = (
    #     ('OWNER', 'OWNER'),
    #     ('REVIEWER', 'REVIEWER')
    # )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # role = models.CharField(max_length=255, blank=True, null=True, choices=ROLES)
    # username = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=15, unique=True,blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]
    objects = UserManager()

    def __str__(self):
        if self.first_name:
            return "{}".format(self.first_name)
        return "{}".format(self.phone_no)

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=365)

        token = jwt.encode({
            'id': str(self.pk),
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
