import hashlib
import random
import re

import time

from django.core import paginator
from django.http import JsonResponse

from myapp import common
from myapp.common import ch_login
from myapp.models import User
from myapp.const import *


def register(request):
    if request.method == 'POST':
        rusername = request.POST.get("username", '0')
        rpwd = request.POST.get("password", '0')
        rpwd2 = request.POST.get("password2", '0')
        client = request.POST.get("client", 'app')
        if rpwd != rpwd2:
            return JsonResponse(common.build_result(CLIENT_ERROR, "两次密码不相同"), safe=False)
        if len(rusername) < 3 or len(rpwd) < 3:
            return JsonResponse(common.build_result(CLIENT_ERROR, "用户名或密码太短"),
                                safe=False)
        if re.match("^[0-9a-zA-Z_]{1,}$", rusername) is None:
            return JsonResponse(common.build_result(CLIENT_ERROR, "用户名不符合规范"), safe=False)
        qr = User.objects.filter(name=rusername)
        if len(qr) > 0:
            return JsonResponse(common.build_result(FATAL_WORK, "已存在该用户"), safe=False)
        isalt = random.randint(100000, 999999)
        curtime = int(round(time.time() * 1000))
        iuserid = "uid%d" % curtime
        # 加盐，计算存储密码
        ipwd = hashlib.md5(("%d-%s" % (isalt, rpwd)).encode(encoding='UTF-8')).hexdigest()
        itoken = common.create_token(iuserid, ipwd, client)
        from myapp import const
        iavatar = const.inner_headers[random.randint(0, len(const.inner_headers) - 1)]
        r_nickname = const.inner_nicknames[random.randint(0, len(const.inner_nicknames) - 1)]
        u = User(userId=iuserid, pwd=ipwd, name=rusername, avatar=iavatar, salt=isalt, token=itoken
                 , nickname=r_nickname)
        u.save()
        return JsonResponse(common.build_model_data(u), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


def login(request):
    if request.method == 'POST':
        rusername = request.POST.get("username", '0')
        rpwd = request.POST.get("password", '0')
        client = request.POST.get("client", 'app')
        if len(rusername) < 3 or len(rpwd) < 3:
            return JsonResponse(common.build_result(CLIENT_ERROR, "用户名或密码太短"),
                                safe=False)
        if re.match("^[0-9a-zA-Z_]{1,}$", rusername) is None:
            return JsonResponse(common.build_result(CLIENT_ERROR, "用户名不规范"), safe=False)
        qr = User.objects.filter(name=rusername)
        if len(qr) == 0:
            return JsonResponse(common.build_result(CLIENT_ERROR, NO_THIS_USER), safe=False)
        u = qr.first()
        if not isinstance(u, User):
            return JsonResponse(common.build_result(NO_RESOURCE, NO_THIS_USER), safe=False)
        # 通过盐和传来的密码，算出存储的密码
        isalt = u.salt
        ipwd = hashlib.md5(("%d-%s" % (isalt, rpwd)).encode(encoding='UTF-8')).hexdigest()
        if u.pwd != ipwd:
            return JsonResponse(common.build_result(NO_AUTH, "密码错误"), safe=False)
        u.token = common.create_token(u.userId, u.pwd, client)
        u.save()
        return JsonResponse(common.build_model_data(u), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


def allusers(request):
    if request.method == 'POST':
        admintoken = request.POST.get("admintoken", '0')
        pageNum = request.POST.get("page", '1')
        if admintoken == "I am cysion":
            qr = User.objects.all()
            pt = paginator.Paginator(qr, 10)
            pages = pt.page(pageNum)
            return JsonResponse(common.build_model_list(pages), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)


@ch_login
def getuser(request):
    r_userid = request.META.get("HTTP_USERID", "")
    qr = User.objects.filter(userId=r_userid)
    return JsonResponse(common.build_model_data(qr[0]), safe=False)


@ch_login
def update_user(request):
    if request.method == 'POST':
        post = request.POST
        r_desc = None
        r_avatar = None
        r_nickname = None
        if "desc" in post:
            r_desc = request.POST.get("desc")
        if "avatar" in post:
            r_avatar = request.POST.get("avatar")
        if "nickname" in post:
            r_nickname = request.POST.get("nickname")
        r_userid = request.META.get("HTTP_USERID", "")
        qr = User.objects.filter(userId=r_userid)
        user = qr[0]
        if r_desc is not None:
            user.selfDesc = r_desc
        if not r_avatar is None:
            user.avatar = r_avatar
        if not r_nickname is None:
            user.nickname = r_nickname
        user.save()
        return JsonResponse(common.build_model_data(qr[0]), safe=False)
    return JsonResponse(common.build_result(CLIENT_ERROR, ERROR_REQ_METHOD), safe=False)
