#-*- coding: utf-8 -*-
from django.shortcuts import render
from  django.views.generic import CreateView, UpdateView, ListView, DetailView


class GenericListView(ListView):
	template_name = None
	paginate_by = 20

	def get_template_names(self, *args, **kwargs):
		if not self.template_name:
			return '%s/%s_list.html' % (self.model._meta.app_label, self.model._meta.object_name.lower())
		return self.template_name


class GenericCreateView(CreateView):
	template_name = None
	paginate_by = 20

	def get_template_names(self, *args, **kwargs):
		if not self.template_name:
			return '%s/%s_create.html' % (self.model._meta.app_label, self.model._meta.object_name.lower())
		return self.template_name


class GenericDetailView(DetailView):
	template_name = None
	paginate_by = 20

	def get_template_names(self, *args, **kwargs):
		if not self.template_name:
			return '%s/%s_detail.html' % (self.model._meta.app_label, self.model._meta.object_name.lower())
		return self.template_name


class GenericUpdateView(UpdateView):
	template_name = None
	paginate_by = 20

	def get_template_names(self, *args, **kwargs):
		if not self.template_name:
			return '%s/%s_update.html' % (self.model._meta.app_label, self.model._meta.object_name.lower())
		return self.template_name