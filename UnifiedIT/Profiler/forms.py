from django import forms
from .models import *

class DepartmentForm(forms.ModelForm):
	class Meta:
		model= Department
		fields = ('name','dept_code')

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields=('street','city','state','pincode')