#-*- coding: utf-8 -*-
from django.shortcuts import render

from core.views import GenericListView, GenericUpdateView, GenericDetailView, GenericCreateView

from .models import Organization
from .forms import OrganizationForm


class OrganizationCreateView(GenericCreateView):
	template_name = 'organization/organization_create.html'
	model = Organization
	form_class = OrganizationForm

	def get_form(self, form_class):
		return form_class(self.request, **self.get_form_kwargs())


class OrganizationUpdateView(GenericUpdateView):
	template_name = 'organization/organization_update.html'
	model = Organization
	form_class = OrganizationForm

	def get_form(self, form_class):
		return form_class(self.request, **self.get_form_kwargs())


class OrganizationListView(GenericListView):
	model = Organization
	paginate_by = 20

	def get_queryset(self, *args, **kwargs):
		return self.model.objects.filter(members__id=self.request.user.id)


class OrganizationDetailView(GenericDetailView):
	template_name = 'organization/organization_detail.html'
	model = Organization
	paginate_by = 20

