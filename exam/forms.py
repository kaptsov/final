from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, CharField




class UserForm(ModelForm):
	password = CharField( widget=PasswordInput, label='Пароль')
	class Meta(object):
		model = User
		fields = ['username', 'email', 'password']
		
        

	
	
			