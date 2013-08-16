from django.contrib import admin
from .models import File, Document

admin.site.register([File, Document])