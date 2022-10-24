from django.urls import path, include
from . import views

urlpatterns = [
    path('about-us/', views.about),
    path('asd/', views.asd),
    path('', views.main),
    path('hacks/', views.hacks),
]
