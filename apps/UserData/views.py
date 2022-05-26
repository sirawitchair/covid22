from django.contrib.auth.views import LoginView
from .forms import MyAuthForm


class MyLoginView(LoginView):    
    authentication_form = MyAuthForm
    template_name = 'login.html'


