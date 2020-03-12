
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

#class RegForm(forms.Form):
#	email = forms.EmailField(max_length=254, help_text='')
#	username = forms.CharField(max_length = 100, help_text='')
#	password1 = forms.CharField(max_length = 100, help_text='')
#	password2 = forms.CharField(max_length = 100, help_text='')

class RegForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='')
	username = forms.CharField(max_length = 100, help_text='')
	password1 = forms.CharField(max_length = 100, help_text='')
	password2 = forms.CharField(max_length = 100, help_text='')

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', ]
#	def save(self):
#		new_save = Users.objects.create(
#			email = self.cleaned_data['email'],
#			username = self.cleaned_data['username'],
#			password1 = self.cleaned_data['password1'],
#			password2 = self.cleaned_data['password2'],
#		)
#
#		return new_save

#	class Meta:
#		model = Users
#		fields = ('email', 'username', 'password1', 'password2', )

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(max_length = 100)


class FixAccountForm(forms.Form):
	username = forms.CharField(max_length=15)
	email = forms.EmailField(max_length=254, help_text='')
	birth_date = forms.DateTimeField()
	location = forms.CharField(max_length=30)
	about_me =  forms.CharField(widget=forms.Textarea, max_length=1000)
	image = forms.FileField()

	class Meta:
		model = User
		fields = ('username', 'email', 'birth_date', 'location', 'about_me', )


	def save(self):
		new_save = User.objects.create(
			email = self.cleaned_data['email'],
			username = self.cleaned_data['username'],
			birth_date = self.cleaned_data['birth_date'],
			location = self.cleaned_data['location'],
			about_me = self.cleaned_data['about_me'],
		)

		return new_save