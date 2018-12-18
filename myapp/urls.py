from django.urls import path

from myapp.view import views,blog_view,userview

urlpatterns = [
    path('index', views.index),
    path('register', userview.register),
    path('login', userview.login),
    path('allusers', userview.allusers),
    path('addlooper', views.add_looper),
    path('toploopers', views.get_looper),
    path('blog/add', blog_view.create_blog),
    path('getblogs', blog_view.get_blogs),
    path('blog/<int:blog_id>', blog_view.get_blog),
]
