from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mobjects import views

urlpatterns = [
    path('mobjects/', views.mobject_list),
    path('mobjects/<int:pk>', views.mobject_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)