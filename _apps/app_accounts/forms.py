from django import forms
from django.db import models
from .models import LogIn

class LoginForm(forms.ModelForm):
    class Meta:
        model=LogIn
        fields = '__all__'

    
    