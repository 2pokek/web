from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('asd/', views.asd),
    path('main/', views.main),
]
