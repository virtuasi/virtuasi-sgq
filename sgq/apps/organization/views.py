#-*- coding: utf-8 -*-
from django.shortcuts import render
from  django.views.generic import CreateView, UpdateView, ListView, DetailView


from .models import Organization
from .forms import OrganizationForm


class OrganizationCreateView(CreateView):
	template_name = 'organization/organization_create.html'
	model = Organization
	form_class = OrganizationForm

	def get_form(self, form_class):
		return form_class(self.request, **self.get_form_kwargs())


class OrganizationUpdateView(UpdateView):
	template_name = 'organization/organization_update.html'
	model = Organization
	form_class = OrganizationForm

	def get_form(self, form_class):
		return form_class(self.request, **self.get_form_kwargs())


class OrganizationListView(ListView):
	template_name = 'organization/organization_list.html'
	model = Organization
	paginate_by = 20


class OrganizationDetailView(DetailView):
	template_name = 'organization/organization_detail.html'
	model = Organization
	paginate_by = 20

