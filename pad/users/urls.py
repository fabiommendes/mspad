from django.contrib.auth import get_user_model
from django.urls import path
from boogie.rest import rest_api

from . import views

# Inclui o modelo User na API
rest_api(get_user_model())

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]
