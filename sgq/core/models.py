#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

from .managers import GenericManager

User = get_user_model()

STATUS = (
    (True,'Ativo'),
    (False,'Inativo'),
)

CONTACT_TYPE = (
    ('PA','particular'),
    ('PR','professional'),
)

class GenericModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(User)
    status = models.BooleanField(
        db_index=True,
        default=True,
        choices=STATUS,
        help_text="Informa se o registro está ativo ou inativo."
    )
    objects = models.Manager()
    values = GenericManager()

    class Meta:
        abstract = True


class OrganizationGenericModel(GenericModel):
    organization = models.ForeignKey('organization.Organization')
