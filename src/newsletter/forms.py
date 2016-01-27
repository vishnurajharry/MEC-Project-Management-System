from django.contrib.auth.models import User
from django import forms
from .models import signup, sellerprofile,notifications


class SignUpForm(forms.ModelForm):
	class Meta:
		model = signup
		fields=['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		print email
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code.
		return full_name


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password')

class sellerProfileForm(forms.ModelForm):
	class Meta:
		model = sellerprofile
		fields=['company','addressline1','addressline2']

class loginForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(widget=forms.PasswordInput())

class NotificationForm(forms.ModelForm):
	class Meta:
		model = notifications
		fields=['notification']
		widgets = {
            'notification': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
	