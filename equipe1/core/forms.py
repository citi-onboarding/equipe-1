from django import forms
from .models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from .models import User
from django.utils.translation import ugettext_lazy as _
from  django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['name', 'username', 'telefone','password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
'''
    class Meta:
        model = User
        fields = ['username', 'password']
'''
