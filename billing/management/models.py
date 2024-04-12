from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.db.models import Q
from django.db.models.signals import post_save,pre_save
from django.utils import timezone
import pytz




class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=0)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True  


class Product(BaseModel):

    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=50)
    price = models.FloatField()
    description=models.TextField(null=True,blank=True)




