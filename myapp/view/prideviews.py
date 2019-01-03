
from django.http import JsonResponse

from myapp import common
from myapp.common import ch_login
from myapp.models import MicroBlog, Pride
from myapp.const import *


@ch_login
def pride_blog(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(NO_RESOURCE, "博客不存在"), safe=False)
        blog = mqr[0]
        qr2 = Pride.objects.filter(blogId=r_blogid)
        if not qr2.exists():
            blog.prideCount = blog.prideCount + 1
            blog.save()
            Pride(blogId=r_blogid, authorId=r_userid).save()
            return JsonResponse(common.build_result(SUCCESS, "success"))
        if qr2.filter(authorId=r_userid).exists():
            return JsonResponse(common.build_result(FATAL_WORK, "已经点过赞了"), safe=False)
        else:
            blog.prideCount = blog.prideCount + 1
            blog.save()
            # 增加点赞记录
            Pride(blogId=r_blogid, authorId=r_userid).save()
            return JsonResponse(common.build_result(SUCCESS, "success"))
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


@ch_login
def un_pride_blog(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_blogid = request.POST.get("blogId", '')
        mqr = MicroBlog.objects.filter(blogId=r_blogid)
        if not mqr.exists():
            return JsonResponse(common.build_result(NO_RESOURCE, "博客不存在"), safe=False)
        blog = mqr[0]
        qr2 = Pride.objects.filter(blogId=r_blogid)
        if not qr2.exists():
            return JsonResponse(common.build_result(FATAL_WORK, "没有点过赞"), safe=False)
        rela = qr2.filter(authorId=r_userid)
        if rela.exists():
            blog.prideCount = blog.prideCount - 1
            blog.save()
            # //删除点赞记录
            rela[0].delete()
            return JsonResponse(common.build_result(SUCCESS, "success"))
        else:
            return JsonResponse(common.build_result(FATAL_WORK, "还没有点过赞"), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)
