from django.db import models

# Create your models here.
class BaseModel(models.Model):
    createTime = models.DateTimeField("创建时间",auto_now_add=True)
    modifyTime = models.DateTimeField("更新时间",auto_now=True)


class User(BaseModel):
    userId = models.CharField("用户id",max_length=20,unique=True)
    pwd = models.CharField("加盐密码",max_length=200)
    token = models.CharField("口令",max_length=120)
    salt = models.IntegerField()
    name = models.CharField("用户名",max_length=20)
    selfDesc = models.CharField("用户描述",max_length=200,null=True)
    avatar = models.CharField("用户头像",max_length=500)

class Looper(BaseModel):
    type = models.CharField("类型",max_length=30)
    mediaId = models.CharField("媒体Id",max_length=30)
    title = models.CharField("标题",max_length=200)
    link = models.CharField("链接",max_length=300)
    picUrl = models.CharField("图片地址",max_length=300)


class Blog(BaseModel):
    text = models.CharField("正文",max_length=200)
    authorId = models.CharField("作者id",max_length=20)
    authorHead = models.CharField("作者头像",max_length=2000)
