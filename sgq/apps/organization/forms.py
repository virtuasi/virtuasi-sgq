from django import forms
from .models import Organization
from core.forms import OrganizationGenericForm


class OrganizationForm(OrganizationGenericForm):

	class Meta:
		model = Organization
		fields = (
			'name',
			'description',
			'site',
		)


