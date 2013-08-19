#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

from core.models import OrganizationGenericModel
from .choices import SECRETIVENESS


User = get_user_model()

def upload_file(dir):
    def upload(object, filename, dir=dir):
        organization = str(object.organization.id)
        path = os.path.join('organizations', organization, dir, filename)
        return path
    return upload


class File(OrganizationGenericModel):
    document = models.ForeignKey('Document', related_name='files')
    version = models.IntegerField(editable=False) # criar automativamente
    content = models.TextField()
    file = models.FileField(upload_to=upload_file('documents/files'))
    modification_description = models.CharField(max_length=250)
    finished = models.BooleanField(default=False)

    class Meta:
        unique_together = (('document','version'),)

    def __unicode__(self):
        return self.versao


class Category(OrganizationGenericModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories' )


class Document(OrganizationGenericModel):
    title = models.CharField(max_length=100)
    description=  models.CharField(max_length=250, blank=True)
    category = models.ForeignKey('Category', null=True, related_name='categories' )
    secretiveness = models.IntegerField(choices=SECRETIVENESS)

    def __unicode__(self):
        return self.titulo

    def current_version(self):
        return self.files.latest('version')
