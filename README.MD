##### KtDevBox项目的后端项目

### 主域名

www.cysion.club/app/


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










































