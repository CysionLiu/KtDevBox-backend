
>本页面包含2个接口，分别为评论博客，评论列表

主域名：http://148.70.2.189/app/


#### 1.评论博客

**路径**：主域名+blog/comment

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
parentId | 博客id|是
content | 评论内容|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success"
}
```

---


#### 2.评论列表

**路径**：主域名+blog/comments/list

**方法**：POST

**Header**：需要

**参数**：


字段  | 说明 | 是否必传
---|---|---
parentId | 博客id|是

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": [
        {
            "parentId": "26d01aa5bd313ee6d3fbdd93bb7c1001",
            "authorId": "uid1550471899901",
            ...
        },
        {
            "parentId": "26d01aa5bd313ee6d3fbdd93bb7c1001",
            "authorId": "uid1550471899901",
            ...
        }
    ]
}
```

---