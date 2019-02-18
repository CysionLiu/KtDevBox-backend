
>本页面包含2个接口，分别为获取某个用户的详细信息，获得轮播信息列表

主域名：http://148.70.2.189/app/


#### 1.获取某个用户详情

**路径**：主域名+userinfo

**方法**：POST

**Header**：可选

**参数**：

application/json格式

示例：

{"userid":"uid1550471899901"}

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": {
        "userId": "uid1550471899901",
        "name": "xushu",
        "nickname": "诸葛武侯",
        "selfDesc": "说明",
        "avatar": "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1545731733&di=82f02933fc19a4ce267617ba3415dadf&src=http://img1.cache.netease.com/catchpic/8/87/8794AABEB648A5B31AD3DD697DE447D2.jpg",
        "createStamptime": "2019-02-18 14:38:19",
        "modifyStamptime": "2019-02-18 16:18:33",
        "blogs": [
            {
                "blogId": "26d01aa5bd313ee6d3fbdd93bb7c1001",
                "title": "测试666",
                ...
                
            },
            {
                "blogId": "ddac6411417d9146b017fa470117558e",
                "title": "测试8",
                "text": "。。",
                "authorId": "uid1550471899901",
                ...
            }
        ]
    }
}
```

---


#### 2.获得轮播信息

**路径**：主域名+toploopers

**方法**：POST/GET

**Header**：不需要

**参数**：

无

**返回值示例**：
```
{
    "code": 200,
    "msg": "success",
    "data": [
        {
            "type": "music",
            "mediaId": "public_tuijian_autumn",
            "title": "秋日私语",
            "link": "\"\"",
            "picUrl": "http://hiphotos.qianqian.com/ting/pic/item/b3119313b07eca80b93485cf932397dda14483e1.jpg",
            "createStamptime": "2018-12-15 22:53:37",
            "modifyStamptime": "2019-01-04 10:01:59"
        },
        {
            "type": "news",
            "mediaId": "\"\"",
            "title": "人类如果进入黑洞，会变成理论上的永生！",
            "link": "https://3g.163.com/all/article/E366FUTB0511C43N.html",
            "picUrl": "http://bjnewsrec-cv.ws.126.net/little72740d9de47545933967705a7275e40cacb.jpeg",
            "createStamptime": "2018-12-16 22:14:25",
            "modifyStamptime": "2018-12-16 22:14:25"
        },
        {
            "type": "blog",
            "mediaId": "777af610f67d009950d0a7475b4472d6",
            "title": "中国迎来首个农民丰收节",
            "link": "\"\"",
            "picUrl": "http://dingyue.nosdn.127.net/FOfTHjbALzIwc6BSiJZGrB6eDv1totpWthQoCkHbOw8Ci1535258643442.jpeg",
            "createStamptime": "2018-12-16 22:15:03",
            "modifyStamptime": "2019-01-05 21:20:31"
        }
    ]
}
```

---