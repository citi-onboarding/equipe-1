from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from .models import User
import lepl.apps.rfc3696
from django.utils.translation import ugettext_lazy as _
from  django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['nome', 'username', 'telefone','email','password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

