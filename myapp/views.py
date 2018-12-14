import hashlib
import random
import time

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp import common
from myapp.models import *
import re

# Create your views here.
from myapp.tool import log


def index(request):
    d = {"name": "welcome"}
    return JsonResponse(d)


# zhu ce
def register(request):
    import base64
    if request.method == 'POST':
        rusername = request.POST.get("username", '0')
        rpwd = request.POST.get("password", '0')
        if len(rusername) < 3 or len(rpwd) < 3:
            return JsonResponse(common.build_result(400, "name or password is too short"), safe=False)
        if re.match("^[0-9a-zA-Z_]{1,}$", rusername) is None:
            return JsonResponse(common.build_result(400, "name is not incorrect"), safe=False)
        qr = User.objects.filter(name=rusername)
        if len(qr) > 0:
            return JsonResponse(common.build_result(401, "name is duplicate"), safe=False)
        isalt = random.randint(1000, 9999)
        log(isalt)
        iuserid = "uid%d" % int(round(time.time() * 1000))
        log(iuserid)
        ipwd = hashlib.md5(("%d-%s" % (isalt, rpwd)).encode(encoding='UTF-8')).hexdigest()
        log(ipwd)
        itoken = base64.b64encode(("%s;%s" % (iuserid, ipwd)).encode("utf-8"))
        itoken = str(itoken,"utf-8")
        from myapp import const
        iavatar = const.inner_headers[random.randint(0, len(const.inner_headers)-1)]
        u = User(userId=iuserid, pwd=ipwd, name=rusername, avatar=iavatar, salt=isalt, token=itoken)
        u.save()
        d={}
        d["name"]=rusername
        d["avatar"] = iavatar
        d["userId"] = iuserid
        d["token"]=itoken
        return JsonResponse(d, safe=False)
    return JsonResponse(common.build_result(400, "error http method"), safe=False)
