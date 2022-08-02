from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HabiTapp.urls'))
]