import hashlib
import random
import re

import time

from django.core import paginator
from django.http import JsonResponse

from myapp import common
from myapp.common import ch_login
from myapp.models import User


def register(request):
    if request.method == 'POST':
        rusername = request.POST.get("username", '0')
        rpwd = request.POST.get("password", '0')
        rpwd2 = request.POST.get("password2", '0')
        client = request.POST.get("client", 'app')
        if rpwd != rpwd2:
            return JsonResponse(common.build_result(400, "two password is not equal"), safe=False)
        if len(rusername) < 3 or len(rpwd) < 3:
            return JsonResponse(common.build_result(400, "name or password is too short"),
                                safe=False)
        if re.match("^[0-9a-zA-Z_]{1,}$", rusername) is None:
            return JsonResponse(common.build_result(400, "name is not incorrect"), safe=False)
        qr = User.objects.filter(name=rusername)
        if len(qr) > 0:
            return JsonResponse(common.build_result(401, "name is duplicate"), safe=False)
        isalt = random.randint(100000, 999999)
        curtime = int(round(time.time() * 1000))
        iuserid = "uid%d" % curtime
        ipwd = hashlib.md5(("%d-%s" % (isalt, rpwd)).encode(encoding='UTF-8')).hexdigest()
        itoken = common.create_token(iuserid, ipwd, client)
        from myapp import const
        iavatar = const.inner_headers[random.randint(0, len(const.inner_headers) - 1)]
        u = User(userId=iuserid, pwd=ipwd, name=rusername, avatar=iavatar, salt=isalt, token=itoken)
        u.save()
        return JsonResponse(common.build_model_data(u), safe=False)
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


def login(request):
    if request.method == 'POST':
        rusername = request.POST.get("username", '0')
        rpwd = request.POST.get("password", '0')
        client = request.POST.get("client", 'app')
        if len(rusername) < 3 or len(rpwd) < 3:
            return JsonResponse(common.build_result(400, "name or password is incorrect"),
                                safe=False)
        if re.match("^[0-9a-zA-Z_]{1,}$", rusername) is None:
            return JsonResponse(common.build_result(400, "name is not incorrect"), safe=False)
        qr = User.objects.filter(name=rusername)
        if len(qr) == 0:
            return JsonResponse(common.build_result(401, "no this user"), safe=False)
        u = qr.first()
        if not isinstance(u, User):
            return JsonResponse(common.build_result(500, "no this user"), safe=False)
        isalt = u.salt
        ipwd = hashlib.md5(("%d-%s" % (isalt, rpwd)).encode(encoding='UTF-8')).hexdigest()
        if u.pwd != ipwd:
            return JsonResponse(common.build_result(400, "error password"), safe=False)
        u.token = common.create_token(u.userId, u.pwd, client)
        u.save()
        return JsonResponse(common.build_model_data(u), safe=False)
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


def allusers(request):
    if request.method == 'POST':
        admintoken = request.POST.get("admintoken", '0')
        pageNum = request.POST.get("page", '1')
        if admintoken == "I am cysion":
            qr = User.objects.all()
            pt = paginator.Paginator(qr, 10)
            pages = pt.page(pageNum)
            return JsonResponse(common.build_model_list(pages), safe=False)
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


@ch_login
def getuser(request):
    r_userid = request.META.get("HTTP_USERID", "")
    qr = User.objects.filter(userId=r_userid)
    return JsonResponse(common.build_model_data(qr[0]), safe=False)
