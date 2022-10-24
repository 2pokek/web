from django.urls import path, include
from . import views

urlpatterns = [
    path('about-us/', views.about,name='about'),
    path('asd/', views.asd,name='asd'),
    path('', views.main,name='home'),
    path('hacks/', views.hacks,name='hack'),
]
