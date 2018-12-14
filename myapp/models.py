from django.db import models

# Create your models here.
class BaseModel(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)


class User(BaseModel):
    userId = models.CharField(max_length=20,db_index=True)
    pwd = models.CharField(max_length=200)
    token = models.CharField(max_length=120)
    salt = models.IntegerField()
    name = models.CharField(max_length=20)
    selfDesc = models.CharField(max_length=200,null=True)
    avatar = models.CharField(max_length=500)

