from django.contrib import admin
from django.urls import path, re_path as url, include
from django.conf import settings
from boogie.rest import rest_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rest_api.urls)),
    path('', include('pad.users.urls')),
    path('', include('pad.micropad.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


