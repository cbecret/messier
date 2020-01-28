from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mobjects import views

urlpatterns = [
    path('objects/', views.MobjectList.as_view()),
    path('objects/<int:pk>/', views.MobjectDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)