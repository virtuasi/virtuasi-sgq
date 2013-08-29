#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

from core.models import GenericModel

User = get_user_model()

class Organization(GenericModel):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.TextField(verbose_name='description')
    site = models.URLField(null=True, blank=True, verbose_name='site')
    owners = models.ManyToManyField(User, verbose_name='owners', related_name='organizations')

    @models.permalink
    def get_absolute_url(self):
    	return ('organization_update', (), {'pk': self.pk})
