from django import forms
from .models import Organization


class OrganizationForm(forms.ModelForm):

	class Meta:
		model = Organization
		fields = (
			'name',
			'description',
			'site',
		)

	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(OrganizationForm, self).__init__(*args, **kwargs)

	def save(self, commit=True, *args, **kwargs):
		obj = super(OrganizationForm, self).save(commit=False, *args, **kwargs)
		if not self.instance.pk:
			obj.owner = self.request.user
		obj.author = self.request.user
		if commit:
			obj.save()
		return obj
