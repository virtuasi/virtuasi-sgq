from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'core.views.index'),
	url(r'organization/', include('apps.organization.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
