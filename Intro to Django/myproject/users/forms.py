form django import forms
form django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 65)
    password = forms.CharField(max_length = 65, widget = forms.PassswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAttributeSimilarityValidatorfields = ['username', 'email', 'password1', 'password2']