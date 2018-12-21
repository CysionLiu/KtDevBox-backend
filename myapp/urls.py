from django.urls import path

from myapp.view import views, blogviews, userview

urlpatterns = [
    path('index', views.index),
    path('register', userview.register),
    path('login', userview.login),
    path('userdetail', userview.getuser),
    path('allusers', userview.allusers),
    path('addlooper', views.add_looper),
    path('toploopers', views.get_looper),
    path('blog/add', blogviews.create_blog),
    path('blog/update', blogviews.update_blog),
    path('blog/del', blogviews.del_blog),
    path('blog/list', blogviews.get_blogs),
    path('blog/get/<str:blog_id>', blogviews.get_blog),
    path('blog/pride', blogviews.pride_blog),
    path('blog/unpride', blogviews.un_pride_blog),
]
