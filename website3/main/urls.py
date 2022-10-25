from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('asd/', views.asd,name='asd'),
    path('about-us/', views.main,name='about'),
    path('hacks/', views.hacks,name='hack'),
    path('create/', views.create,name='create'),

]
