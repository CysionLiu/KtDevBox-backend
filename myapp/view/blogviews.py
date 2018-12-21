import hashlib
import random
import time
from django.core import paginator
from django.http import JsonResponse

from myapp import common, const
from myapp.common import ch_login
from myapp.models import User, MicroBlog, Pride


@ch_login
def create_blog(request):
    if request.method == 'POST':
        params = request.POST
        if "title" not in params:
            return JsonResponse(common.build_result(400, "lack title"), safe=False)
        r_userid = request.META.get("HTTP_USERID")
        r_text = request.POST.get("text", '0')
        r_title = request.POST.get("title", '')
        qr = User.objects.filter(userId=r_userid)
        if len(qr) == 0:
            return JsonResponse(common.build_result(401, "no this user"), safe=False)
        u = qr[0]
        avatar = const.inner_headers[random.randint(0, len(const.inner_headers) - 1)]
        ran = random.randint(1, 100)
        curtime = int(round(time.time() * 1000))
        r_blogid = hashlib.md5(
            ("%s-%d-%s" % (r_userid, ran, curtime)).encode(encoding='UTF-8')).hexdigest()
        MicroBlog(blogId=r_blogid, title=r_title, text=r_text, icon=avatar,
                  authorId=r_userid).save()
        return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


@ch_login
def update_blog(request):
    if request.method == 'POST':
        params = request.POST
        if "title" not in params:
            return JsonResponse(common.build_result(400, "lack title"), safe=False)
        r_userid = request.META.get("HTTP_USERID")
        r_text = request.POST.get("text", '')
        r_blogid = request.POST.get("blogId", '')
        r_title = request.POST.get("title", '')
        qr = User.objects.filter(userId=r_userid)
        if not qr.exists():
            return JsonResponse(common.build_result(401, "no this user"), safe=False)
        if r_userid != qr[0].userId:
            return JsonResponse(common.build_result(503, "unknown"), safe=False)
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(404, "blog does not exist"), safe=False)
        blog = mqr[0]
        if len(r_title) > 0:
            blog.title = r_title
        if len(r_text) > 0:
            blog.text = r_text
        blog.save()
        return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


@ch_login
def del_blog(request):
    if request.method == 'POST':
        params = request.POST
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        qr = User.objects.filter(userId=r_userid)
        if not qr.exists():
            return JsonResponse(common.build_result(401, "no this user"), safe=False)
        if r_userid != qr[0].userId:
            return JsonResponse(common.build_result(503, "unknown"), safe=False)
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(404, "blog does not exist"), safe=False)
        blog = mqr[0]
        blog.delete()
        return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


@ch_login
def pride_blog(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(404, "blog does not exist"), safe=False)
        blog = mqr[0]
        qr2 = Pride.objects.filter(blogId=r_blogid)
        if not qr2.exists():
            blog.prideCount = blog.prideCount + 1
            blog.save()
            Pride(blogId=r_blogid, authorId=r_userid).save()
            return JsonResponse(common.build_result(200, "success"))
        if qr2.filter(authorId=r_userid).exists():
            return JsonResponse(common.build_result(404, "已经点过赞了"), safe=False)
        else:
            blog.prideCount = blog.prideCount + 1
            blog.save()
            # 增加点赞记录
            Pride(blogId=r_blogid, authorId=r_userid).save()
            return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


@ch_login
def un_pride_blog(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(404, "blog does not exist"), safe=False)
        blog = mqr[0]
        qr2 = Pride.objects.filter(blogId=r_blogid)
        if not qr2.exists():
            return JsonResponse(common.build_result(404, "没有点过赞"), safe=False)
        rela = qr2.filter(authorId=r_userid)
        if rela.exists():
            blog.prideCount = blog.prideCount - 1
            blog.save()
            # //删除点赞记录
            rela[0].delete()
            return JsonResponse(common.build_result(200, "success"))
        else:
            return JsonResponse(common.build_result(404, "已经点过赞了"), safe=False)
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


def get_blog(request, blog_id):
    qr = MicroBlog.objects.filter(blogId=blog_id)
    if len(qr) == 0:
        return JsonResponse(common.build_result(401, "no  blog"), safe=False)
    blog = qr.first()
    return JsonResponse(common.build_model_data(blog), safe=False)


def get_blogs(request):
    pageNum = 1
    if request.method == 'POST':
        pageNum = request.POST.get("page", '1')
    if request.method == 'GET':
        pageNum = request.GET.get("page", '1')
    if pageNum == 0:
        pageNum = 1
    qr = MicroBlog.objects.all().filter(isDeleted=0).order_by("createTime")
    pt = paginator.Paginator(qr, 10)
    pages = pt.page(pageNum)
    return JsonResponse(common.build_model_list(pages), safe=False)
