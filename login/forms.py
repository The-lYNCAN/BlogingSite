from django import forms
from login.models import blog_model, comments
from django.contrib.auth.models import User

class signup_form(forms.ModelForm):
    username = forms.CharField(max_length=256)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class login_form(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256)


class commenting(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('content',)