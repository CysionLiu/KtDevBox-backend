from django.core import paginator
from django.http import JsonResponse

from myapp import common
from myapp.models import User, Blog


def create_blog(request):
    if request.method == 'POST':
        params = request.POST
        if "text" not in params:
            return JsonResponse(common.build_result(400, "lack text"), safe=False)
        r_userid = request.META.get("HTTP_USERID")
        if r_userid is None:
            return JsonResponse(common.build_result(400, "lack userid in header"), safe=False)
        r_text = request.POST.get("text", '0')
        qr = User.objects.filter(userId=r_userid)
        if len(qr) == 0:
            return JsonResponse(common.build_result(401, "unlogin"), safe=False)
        u = qr.first()
        if isinstance(u, User):
            avatar = u.avatar
        Blog(text=r_text, authorHead=avatar, authorId=r_userid).save()
        return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


def get_blog(request, blog_id):
    qr = Blog.objects.filter(pk=blog_id)
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
    qr = Blog.objects.all()
    pt = paginator.Paginator(qr, 10)
    pages = pt.page(pageNum)
    return JsonResponse(common.build_model_list(pages), safe=False)
