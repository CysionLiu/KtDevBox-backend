from django.urls import path

from myapp import views

urlpatterns = [
    path('index', views.index),
    path('register', views.register),
    path('login', views.login),
    path('allusers', views.allusers),
    path('addlooper', views.add_looper),
    path('toploopers', views.get_looper),
]
