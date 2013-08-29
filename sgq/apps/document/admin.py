from django.contrib import admin
from .models import File, Document, Category


admin.site.register([File, Document, Category])