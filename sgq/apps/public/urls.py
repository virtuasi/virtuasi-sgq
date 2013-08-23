from django.conf.urls import patterns, url

urlpatterns = patterns('apps.public.views',
    url(r'^$', 'home', name='public_home'),
)
