from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from mobjects import views


router = DefaultRouter()
router.register(r'mobjects', views.MobjectViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]