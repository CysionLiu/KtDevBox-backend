from django.contrib import admin

# Register your models here.
from myapp.models import User, Looper

admin.site.register(User)
admin.site.register(Looper)