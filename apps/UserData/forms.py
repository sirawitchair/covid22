from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext as _

class MyAuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(MyAuthForm,self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = { 'autofocus': True,
                    'class' : 's2-txt1 placeholder0 input100',
                    'id' : 'username',
                    'placeholder' : 'email ทอ. ไม่มี @rtaf.mi.th'}))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                    'class' : 's2-txt1 placeholder0 input100',
                    'placeholder' : 'password',
                    'id' : 'password'                                    
                    })
    )
