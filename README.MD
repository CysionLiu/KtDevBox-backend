
### 一套免费、简单、逻辑比较全面的接口


开发基于Python 3.6 - Django 2.14，已部署至一个简单的服务器，基于Centos+uwsgi+nginx

域名备案比较麻烦，练手之用，就不备案了，**完全不影响使用**。

网上常见的免费接口，多为GET请求，一般不支持POST方法，POST json数据或者Header头参数，本项目主要补充这方面需求，服务于感兴趣的童鞋。


[一个安卓项目KtDevBox，用到了这里面所有的接口，感兴趣的可以看看](https://github.com/CysionLiu/KtDevBox)



### 主域名

http://47.94.100.160/app/



### 公共Header

若需要，则必传，目前是两个字段：

userid 和 token


### 接口列表

- [用户相关信息](./apidoc/user.md)
- [博客增删改查](./apidoc/blog.md)
- [博客点赞相关](./apidoc/pride.md)
- [博客收藏相关](./apidoc/collect.md)
- [博客评论相关](./apidoc/comment.md)
- [其它，轮播等](./apidoc/other.md)



### 状态码

对应返回值json里面的code字段:


200 表示请求成功，获得了正确的json;

400 表示客户端错误，一般是指方法不对或者传错参数

402 错误的操作 一般指逻辑上失败，比如没有点过赞时，执行点赞操作；

403 没有权限，比如用户删除非自己的博客；

404 没有找到资源；

500 服务器逻辑处理错误(若发生，需issue下)；

### 返回格式示例
```
{
    "code": 200,
    "msg": "success"
    "data":"主体数据(可能没有该字段)"
}
```



### 觉的不错，请右上角Star一下



### License

Copyright 2019 CysionLiu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.






