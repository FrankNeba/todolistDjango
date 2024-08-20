from .models import Todo
from django import forms
# from django.contrib.auth.models import User

class todocreates(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'image']


class Loginform(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['username', 'password']