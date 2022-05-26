from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from apps.UserData.views import MyLoginView


urlpatterns = [
    # path('gadmin/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', include('apps.Patient.urls')),
    
    path('login/', MyLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
