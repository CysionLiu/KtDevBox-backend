import xadmin
from django.contrib import admin

# Register your models here.
from myapp.models import User, Looper, MicroBlog

#
# admin.site.register(User)
# admin.site.register(Looper)


xadmin.site.register(User)
xadmin.site.register(Looper)
xadmin.site.register(MicroBlog)
