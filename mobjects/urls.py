from django.urls import path
from mobjects import views

urlpatterns = [
    path('objects/', views.mobject_list),
    path('objects/<int:pk>/', views.mobject_detail),
]