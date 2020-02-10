from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include


# Définition des routes globales de l'API
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/v1/', include('mobjects.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
