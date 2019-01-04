from django.urls import path

from myapp.view import views, blogviews, userview, prideviews, collectviews, commentviews

urlpatterns = [
    path('index', views.index),
    path('register', userview.register),
    path('login', userview.login),
    path('userdetail', userview.getuser),
    path('updateuser', userview.update_user),
    path('allusers', userview.allusers),
    path('addlooper', views.add_looper),
    path('toploopers', views.get_looper),
    path('blog/add', blogviews.create_blog),
    path('blog/update', blogviews.update_blog),
    path('blog/del', blogviews.del_blog),
    path('blog/list', blogviews.get_blogs),
    path('blog/userlist', blogviews.get_user_blogs),
    path('blog/get/<str:blog_id>', blogviews.get_blog),
    path('blog/pride', prideviews.pride_blog),
    path('blog/unpride', prideviews.un_pride_blog),
    path('blog/collect', collectviews.collect),
    path('blog/uncollect', collectviews.un_collect),
    path('blog/iscollected', collectviews.is_collected),
    path('blog/collections', collectviews.get_collections),
    path('blog/comment', commentviews.comment),
    path('blog/comments/list', commentviews.get_comments),
]
