
>本页面包含4个接口，分别为用户注册、登录、获取用户信息和更新用户信息

#### 用户注册

**路径**：主域名+register

**方法**：POST

**Header**：不传

**参数**：

字段  | 说明 | 是否必传
---|---|---
username | 用户名(非昵称)，唯一，3个以上数字字母下划线|是
password | 密码，3个以上数字字母下划线|是
password2 | 确认密码，同password|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1550471907710",
        "token": "dWlkMTU1MDQ3MTkwNzcxMDtjOGViODNiNWViYTg1OTI4MmQ4u",
        "name": "xushu",
        "nickname": "黄汉升",
        ...
    }
}
```

---

#### 用户登录

**路径**：主域名+login

**方法**：POST

**Header**：不传

**参数**：

字段  | 说明 | 是否必传
---|---|---
username | 用户名(非昵称)，唯一，3个以上数字字母下划线|是
password | 密码，3个以上数字字母下划线|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1550471899901",
        "token": "uuu",
        "name": "xushu",
        "nickname": "诸葛亮字孔明",
        "selfDesc": "",
        ...
    }
}
```

---

#### 获取用户自己的信息

**路径**：主域名+userdetail

**方法**：GET

**Header**：需要

**参数**：
无

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1550471907710",
        "token": "dWlkMTU1MDQ3MTkwNzcxMDtjOGViODNiNWViYTg1OTI4MmQ4u",
        "name": "xushu",
        "nickname": "黄汉升",
        "selfDesc": "",
        "avatar": ""
        ...
    }
}
```

---


#### 更新用户信息

**路径**：主域名+updateuser

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
desc | 用户名描述，200字符以内|否
avatar | 用户头像，500字符以内,http链接|否
nickname | 用户昵称，120字符以内|否

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1550471907710",
        "token": "dWlkMTU1MDQ3MTkwNzcxMDtjOGViODNiNWViYTg1OTI4MmQ4u",
        "name": "xushu",
        "nickname": "黄汉升",
        "selfDesc": null,
        "avatar": ""
        ...
    }
}
```

---






