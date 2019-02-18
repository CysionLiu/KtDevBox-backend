
>本页面包含4个接口，分别为收藏博客，取消收藏，是否收藏以及收藏列表

主域名：http://148.70.2.189/app/


#### 1.收藏博客

**路径**：主域名+blog/collect

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
itemId | 博客id|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success"
}
```

---


#### 2.取消收藏

**路径**：主域名+blog/uncollect

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
itemId | 博客id|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success"
}
```

---


#### 3.是否收藏

**路径**：主域名+blog/iscollected

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
itemId | 博客id|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success"
}
```

---

#### 4.获得收藏列表

**路径**：主域名+blog/collections

**方法**：POST/GET

**Header**：需要

**参数**：

无

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": [
        {
            "itemId": "ddac6411417d9146b017fa470117558e",
            "authorId": "uid1545563190540",
            "colType": 0,
            "linkUrl": "",
            "itemTitle": "测试8",
            "coverImg": "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2052372606,1200247783&fm=179&app=42&f=JPEG?w=121&h=121",
            "isLargeIcon": 0,
            "createStamptime": "2019-02-18 16:54:53",
            "modifyStamptime": "2019-02-18 16:54:53"
        }
    ]
}
```

---