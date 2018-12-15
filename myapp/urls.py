from django.urls import path

from myapp import views

urlpatterns = [
    path('index', views.index),
    path('register', views.register),
    path('login', views.login),
    path('allusers', views.allusers),
]
