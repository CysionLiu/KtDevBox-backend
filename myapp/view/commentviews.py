from django.http import JsonResponse

from myapp import common
from myapp.common import ch_login
from myapp.models import User, Comment, MicroBlog
from myapp.const import *


# 评论，暂时只提供一级评论
@ch_login
def comment(request):
    if request.method == 'POST':
        r_userid = request.META.get("HTTP_USERID")
        r_parentid = request.POST.get("parentId", '')
        r_content = request.POST.get("content", '')
        r_type = request.POST.get("type", 1)
        if len(r_content) == 0:
            return JsonResponse(common.build_result(CLIENT_ERROR, "内容为空"), safe=False)
        q_blog = MicroBlog.objects.filter(blogId=r_parentid)
        if r_type == 1 and len(q_blog) == 0:
            return JsonResponse(common.build_result(CLIENT_ERROR, "博客不存在"), safe=False)
        q_user = User.objects.filter(userId=r_userid)[0]
        Comment(authorId=r_userid, authorName=q_user.nickname,
                authorAvatar=q_user.avatar, parentId=r_parentid,
                content=r_content, type=r_type).save()
        q_blog[0].commentCount = q_blog[0].commentCount + 1
        q_blog[0].save()
        return JsonResponse(common.build_result(SUCCESS, "success"))
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


# 获得评论列表
def get_comments(request):
    r_parentid = ""
    if request.method == 'POST':
        r_parentid = request.POST.get("parentId", '')
    if request.method == 'GET':
        r_parentid = request.GET.get("parentId", '')
    qr = Comment.objects.filter(parentId=r_parentid).order_by("-createTime")
    return JsonResponse(common.build_model_list(qr), safe=False)
