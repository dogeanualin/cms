
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

class MyAuthentication(AuthenticationForm):
    
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "class":"form-control bg-transparent",'placeholder':'username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', "class":"form-control bg-transparent",'placeholder':'password'}),
    )