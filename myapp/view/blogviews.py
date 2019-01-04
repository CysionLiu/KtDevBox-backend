import hashlib
import random
import time
from django.core import paginator
from django.http import JsonResponse

from myapp import common, const
from myapp.common import ch_login
from myapp.models import User, MicroBlog, Pride, Collect
from myapp.const import *


@ch_login
def create_blog(request):
    if request.method == 'POST':
        params = request.POST
        if "title" not in params:
            return JsonResponse(common.build_result(CLIENT_ERROR, LACK_PARAM), safe=False)
        r_userid = request.META.get("HTTP_USERID")
        r_text = request.POST.get("text", '0')
        r_title = request.POST.get("title", '')
        r_icon = request.POST.get("icon", None)
        qr = User.objects.filter(userId=r_userid)
        largeicon = 0
        if len(qr) == 0:
            return JsonResponse(common.build_result(CLIENT_ERROR, NO_THIS_USER), safe=False)
        if r_icon is None:
            r = random.randint(0, 1)
            if r == 0:
                r_icon = const.inner_small_icons[
                    random.randint(0, len(const.inner_small_icons) - 1)]
            else:
                largeicon = 1
                r_icon = const.inner_big_icons[random.randint(0, len(const.inner_big_icons) - 1)]
        ran = random.randint(1, 100)
        curtime = int(round(time.time() * 1000))
        r_blogid = hashlib.md5(
            ("%s-%d-%s" % (r_userid, ran, curtime)).encode(encoding='UTF-8')).hexdigest()
        MicroBlog(blogId=r_blogid, title=r_title, text=r_text, icon=r_icon,
                  authorId=r_userid, isLargeIcon=largeicon).save()
        return JsonResponse(common.build_result(SUCCESS, "success"))
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


@ch_login
def update_blog(request):
    if request.method == 'POST':
        params = request.POST
        if "title" not in params:
            return JsonResponse(common.build_result(CLIENT_ERROR, LACK_PARAM), safe=False)
        r_userid = request.META.get("HTTP_USERID")
        r_text = request.POST.get("text", '')
        r_blogid = request.POST.get("blogId", '')
        r_title = request.POST.get("title", '')
        r_icon = request.POST.get("icon", '')
        qr = User.objects.filter(userId=r_userid)
        if not qr.exists():
            return JsonResponse(common.build_result(NO_AUTH, NO_THIS_USER), safe=False)
        if r_userid != qr[0].userId:
            return JsonResponse(common.build_result(SERVER_ERROR, SERVER_ERROR_MSG), safe=False)
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(NO_RESOURCE, "博客不存在"), safe=False)
        blog = mqr[0]
        if blog.authorId != r_userid:
            return JsonResponse(common.build_result(FATAL_WORK, "无权修改该博客"), safe=False)
        if len(r_title) > 0:
            blog.title = r_title
        if len(r_text) > 0:
            blog.text = r_text
        if len(r_icon) > 0:
            blog.icon = r_icon
        blog.save()
        return JsonResponse(common.build_result(SUCCESS, "success"))
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


@ch_login
def del_blog(request):
    if request.method == 'POST':
        params = request.POST
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        qr = User.objects.filter(userId=r_userid)
        if not qr.exists():
            return JsonResponse(common.build_result(NO_AUTH, NO_THIS_USER), safe=False)
        if r_userid != qr[0].userId:
            return JsonResponse(common.build_result(SERVER_ERROR, SERVER_ERROR_MSG), safe=False)
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(NO_RESOURCE, "博客不存在"), safe=False)
        blog = mqr[0]
        if blog.authorId != r_userid:
            return JsonResponse(common.build_result(FATAL_WORK, "无权删除该博客"), safe=False)
        blog.delete()
        # //删除点赞
        Pride.objects.filter(blogId=r_blogid).delete()
        # 删除收藏
        Collect.objects.filter(itemId=r_blogid).delete()
        return JsonResponse(common.build_result(SUCCESS, "success"))
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


#
def get_blog(request, blog_id):
    r_userid = request.META.get("HTTP_USERID")
    qr = MicroBlog.objects.filter(blogId=blog_id)
    if len(qr) == 0:
        return JsonResponse(common.build_result(NO_RESOURCE, "博客不存在"), safe=False)
    blog = qr[0]
    if len(Pride.objects.filter(authorId=r_userid).filter(blogId=blog_id))>0:
        blog.isPrided=MicroBlog.HAVE
    if len(Collect.objects.filter(authorId=r_userid).filter(itemId=blog_id))>0:
        blog.isCollected=MicroBlog.HAVE
    return JsonResponse(common.build_model_data(blog), safe=False)


def get_blogs(request):
    r_userid = request.META.get("HTTP_USERID")
    pageNum = 1
    if request.method == 'POST':
        pageNum = request.POST.get("page", '1')
    if request.method == 'GET':
        pageNum = request.GET.get("page", '1')
    if pageNum == 0:
        pageNum = 1
    qr = MicroBlog.objects.all().filter(isDeleted=0).order_by("-createTime")
    pt = paginator.Paginator(qr, 10)
    try:
        pages = pt.page(pageNum)
        tmp_pride = Pride.objects.filter(authorId=r_userid)
        tmp_col = Collect.objects.filter(authorId=r_userid)
        for d in pages:
            if isinstance(d, MicroBlog):
                if len(tmp_pride.filter(blogId=d.blogId)) > 0:
                    d.isPrided = MicroBlog.HAVE
                if len(tmp_col.filter(itemId=d.blogId)) > 0:
                    d.isCollected = MicroBlog.HAVE
        return JsonResponse(common.build_model_list(pages), safe=False)
    except:
        return JsonResponse(common.build_result(CLIENT_ERROR, "没有更多数据"), safe=False)


# 获取某个用户的博客列表
@ch_login
def get_user_blogs(request):
    r_userid = request.META.get("HTTP_USERID")
    pageNum = 1
    if request.method == 'POST':
        pageNum = request.POST.get("page", '1')
    if request.method == 'GET':
        pageNum = request.GET.get("page", '1')
    if pageNum == 0:
        pageNum = 1
    qr = MicroBlog.objects.all().filter(authorId=r_userid).filter(isDeleted=0).order_by(
        "-createTime")
    pt = paginator.Paginator(qr, 50)
    try:
        pages = pt.page(pageNum)
        tmp_pride = Pride.objects.filter(authorId=r_userid)
        tmp_col = Collect.objects.filter(authorId=r_userid)
        for d in pages:
            if isinstance(d, MicroBlog):
                if len(tmp_pride.filter(blogId=d.blogId)) > 0:
                    d.isPrided = MicroBlog.HAVE
                if len(tmp_col.filter(itemId=d.blogId)) > 0:
                    d.isCollected = MicroBlog.HAVE
        return JsonResponse(common.build_model_list(pages), safe=False)
    except:
        return JsonResponse(common.build_result(CLIENT_ERROR, "没有更多数据"), safe=False)
