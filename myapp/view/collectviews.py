from django.core import paginator
from django.http import JsonResponse

from myapp import common
from myapp.common import ch_login
from myapp.models import MicroBlog, Collect
from myapp.const import *


# 收藏实体记录（0博客，1新闻【必须要有itemUrl】，2音乐）
@ch_login
def collect(request):
    r_userid = request.META.get("HTTP_USERID")
    type = ""
    itemId = ""
    itemTitle = ""
    itemUrl = ""
    coverImg = ""
    if request.method == 'POST':
        type = request.POST.get("colType", '0')
        itemId = request.POST.get("itemId", '')
        itemTitle = request.POST.get("itemTitle", '')
        itemUrl = request.POST.get("itemUrl", '')
        coverImg = request.POST.get("coverImg", '')
    if request.method == 'GET':
        type = request.GET.get("colType", '0')
        itemId = request.GET.get("itemId", '')
        itemTitle = request.POST.get("itemTitle", '')
        itemUrl = request.POST.get("itemUrl", '')
        coverImg = request.POST.get("coverImg", '')
    if len(itemId) < 2:
        return JsonResponse(common.build_result(CLIENT_ERROR, "id不正确"), safe=False)
    if type == 1:
        if len(itemUrl) < 8 and (not itemUrl.startswith("http")):
            return JsonResponse(common.build_result(CLIENT_ERROR, "缺少参数"), safe=False)

    col_qr = Collect.objects.filter(authorId=r_userid).filter(itemId=itemId)
    if len(col_qr) > 0:
        return JsonResponse(common.build_result(CLIENT_ERROR, "已收藏过"), safe=False)
    # 博客收藏
    if type == "0":
        b_qr = MicroBlog.objects.filter(blogId=itemId)
        if len(b_qr) == 0:
            return JsonResponse(common.build_result(CLIENT_ERROR, "该博客不存在"), safe=False)
        Collect(itemId=itemId, authorId=r_userid, itemTitle=b_qr[0].title
                , linkUrl="", coverImg=b_qr[0].icon, colType=Collect.BLOG,isLargeIcon=b_qr[0].isLargeIcon).save()
        return JsonResponse(common.build_result(SUCCESS, "success"), safe=False)
    # 其它收藏
    else:
        Collect(itemId=itemId, authorId=r_userid, itemTitle=itemTitle
                , linkUrl=itemUrl, coverImg=coverImg,
                colType=Collect.NEWS if (type == "1") else Collect.MUSIC).save()
        return JsonResponse(common.build_result(SUCCESS, "success"), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, "没有更多数据"), safe=False)


# 取消收藏
@ch_login
def un_collect(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_itemId = request.POST.get("itemId", '')
        qr2 = Collect.objects.filter(itemId=r_itemId).filter(authorId=r_userid)
        if not qr2.exists():
            return JsonResponse(common.build_result(FATAL_WORK, "没有收藏过"), safe=False)
        else:
            qr2[0].delete()
            return JsonResponse(common.build_result(SUCCESS, "success"), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


# 判断是否收藏
@ch_login
def is_collected(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_itemId = request.POST.get("itemId", '')
        qr2 = Collect.objects.filter(itemId=r_itemId).filter(authorId=r_userid)
        if not qr2.exists():
            return JsonResponse(common.build_result(FATAL_WORK, "没有收藏过"), safe=False)
        else:
            return JsonResponse(common.build_result(SUCCESS, "已收藏"), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


# 获得个人收藏列表
@ch_login
def get_collections(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_type = request.POST.get("colType", '0')
        qr2 = Collect.objects.filter(authorId=r_userid).filter(colType=r_type)
        return JsonResponse(common.build_model_list(qr2), safe=False)
    if request.method == 'GET':
        r_userid = request.META.get("HTTP_USERID")
        r_type = request.GET.get("colType", '0')
        qr2 = Collect.objects.filter(authorId=r_userid).filter(colType=r_type)
        return JsonResponse(common.build_model_list(qr2), safe=False)
