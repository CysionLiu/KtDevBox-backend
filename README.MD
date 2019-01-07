##### KtDevBox项目的后端项目

开发基于Python 3.6, Django 2.14

已部署至一个简单的服务器，基于Centos+uwsgi+nginx

域名备案比较麻烦，练手之用，就不备案了。

本人主攻方向不是后端，本项目主要是服务于一安卓项目，感兴趣的可以看看：


[KtDevBox](https://github.com/CysionLiu/KtDevBox)


该项目文档完善中。。。



### 主域名

http://148.70.2.189/app/


**1. 注册**

路径： register

方法:  post

header: 无

body:


参数 | 类型 | 是否必填
---|---|---
username | String| 是
password | String| 是
password2 | String| 是


返回值：


```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1545484862347",
        "token": "dWlkMTU0NTQ4NDg2MjM0NzsxZDc0MjBmZDA3NzkzNWU0Nzg2MGY3MGI3MjNhZmY0MDthcHA7MTU0NTQ4NDg2MjM0Nw==",
        "name": "cysion",
        "selfDesc": null,
        "avatar": "https://pic.qqtn.com/up/2018-12/2018121407591215403.jpg",
        "createStamptime": "2018-12-22 21:21:02",
        "modifyStamptime": "2018-12-22 21:21:02"
    }
}

```

**2. 登录**

路径： login

方法:  post

header: 无

body:


参数 | 类型 | 是否必填
---|---|---
username | String| 是
password | String| 是


返回值 ：

```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1545484862347",
        "token": "dWlkMTU0NTQ4NDg2MjM0NzsxZDc0MjBmZDA3NzkzNWU0Nzg2MGY3MGI3MjNhZmY0MDthcHA7MTU0NTQ4NDg5OTA0Ng==",
        "name": "cysion",
        "selfDesc": null,
        "avatar": "https://pic.qqtn.com/up/2018-12/2018121407591215403.jpg",
        "createStamptime": "2018-12-22 21:21:02",
        "modifyStamptime": "2018-12-22 21:21:39"
    }
}
```



**3. 获取用户信息**

路径： userdetail

方法:  post

header:


参数 | 类型 | 是否必填
---|---|---
userid | String| 是
token | String| 是


body: 无

---



**4. 获取轮播**

路径： toploopers

方法:  get

header: 无

body: 无


返回值 ：

```

```

---



**5. 创建博客**

路径： blog/add

方法:  post

header :


参数 | 类型 | 是否必填
---|---|---
userid | String| 是
token | String| 是

body :

参数 | 类型 | 是否必填
---|---|---
title | String| 是
text | String| 否










































