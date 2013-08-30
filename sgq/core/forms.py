#-*- coding: utf-8 -*-
from django import forms

class GenericForm(forms.ModelForm):

	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(GenericForm, self).__init__(*args, **kwargs)

	def save(self, commit=True, *args, **kwargs):
		obj = super(GenericForm, self).save(commit=False, *args, **kwargs)
		obj.author = self.request.user
		if commit:
			obj.save()
		return obj


class OrganizationGenericForm(GenericForm):

	def save(self, commit=True, *args, **kwargs):
		obj = super(OrganizationGenericForm, self).save(commit=False, *args, **kwargs)
		if not self.instance.pk:
			obj.owner = self.request.user
		if commit:
			obj.save()
		return obj
