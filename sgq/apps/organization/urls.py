from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
	url(r'^$', views.OrganizationListView.as_view(), name='organization_list'),
	url(r'^create/$', views.OrganizationCreateView.as_view(), name='organization_create'),
	url(r'^update/(?P<pk>\d+)/$', views.OrganizationUpdateView.as_view(), name='organization_update'),
	url(r'^detail/(?P<pk>\d+)/$', views.OrganizationDetailView.as_view(), name='organization_detail'),
)
