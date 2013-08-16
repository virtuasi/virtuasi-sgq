# -*- coding: utf-8 -*-
from django.db import models

class GenericManager(models.Manager):
    
    def actived(self, *args, **kwargs):
        qs = self.get_query_set().filter(*args, **kwargs)
        return qs.filter(actived=True)
