#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

from core.models import GenericModel

User = get_user_model()

class Organization(GenericModel):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.TextField(verbose_name='description')
    site = models.URLField(verbose_name='site')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='organizations')
