from django.urls import re_path
from rest_framework.routers import DefaultRouter
from boogie.rest import rest_api

from . import views

urlpatterns = [
    re_path(r'^(?P<path>(?:[a-z]+/)*)$', views.folder_list, name='folder-list'),
    re_path(r'^(?P<path>(?:[a-z]+/)*)(?P<name>[a-z]+)(?P<ext>\.[a-z]+)$', views.editor, name='editor'),
    re_path(r'^ajax/postForm/(?P<path>(?:[a-z]+/)*)(?P<name>[a-z]+)(?P<ext>\.[a-z]+)$', views.postForm, name='postForm'),
]
