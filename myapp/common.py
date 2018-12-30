import base64
import time

from myapp.models import User
from myapp.tool import log

from django.http import JsonResponse

from myapp.const import *


def ch_login(func):  # 自定义登录验证装饰器
    def warpper(request, *args, **kwargs):
        userid = request.META.get("HTTP_USERID", "")
        r_token = request.META.get("HTTP_TOKEN", "")
        q = User.objects.filter(userId=userid)
        if not q.exists():
            return JsonResponse(build_result("401", "未登录"))
        if q.first().token == r_token:
            return func(request, *args, **kwargs)
        else:
            return JsonResponse(build_result(NO_AUTH, "token失效，请重新登录"))

    return warpper


def create_token(uid, pwd, type):
    curtime = int(round(time.time() * 1000))
    itoken = base64.b64encode(("%s;%s;%s;%d" % (uid, pwd, type, curtime)).encode("utf-8"))
    itoken = str(itoken, "utf-8")
    return itoken


def build_result(code, msg):
    d = {"code": code, "msg": msg}
    return d


def build_model_data(data):
    r = build_result(200, "success")
    log(data.__dict__)
    if "createTime" in data.__dict__:
        ct = data.__dict__.get("createTime")
        data.__dict__.pop("createTime")
        data.__dict__["createStamptime"] = ct.strftime('%Y-%m-%d %H:%M:%S')
    if "modifyTime" in data.__dict__:
        mt = data.__dict__.get("modifyTime")
        data.__dict__.pop("modifyTime")
        data.__dict__["modifyStamptime"] = mt.strftime('%Y-%m-%d %H:%M:%S')
    if "_state" in data.__dict__:
        data.__dict__.pop("_state")
    if "pwd" in data.__dict__:
        data.__dict__.pop("pwd")
    if "salt" in data.__dict__:
        data.__dict__.pop("salt")
    if "basemodel_ptr_id" in data.__dict__:
        data.__dict__.pop("basemodel_ptr_id")
    if "id" in data.__dict__:
        data.__dict__.pop("id")
    r["data"] = data.__dict__
    log(r)
    return r



def build_model_list(dataList):
    r = build_result(200, "success")
    target = []
    for data in dataList:
        log(data.__dict__)
        if "createTime" in data.__dict__:
            ct = data.__dict__.get("createTime")
            data.__dict__.pop("createTime")
            data.__dict__["createStamptime"] = ct.strftime('%Y-%m-%d %H:%M:%S')
        if "modifyTime" in data.__dict__:
            mt = data.__dict__.get("modifyTime")
            data.__dict__.pop("modifyTime")
            data.__dict__["modifyStamptime"] = mt.strftime('%Y-%m-%d %H:%M:%S')
        if "_state" in data.__dict__:
            data.__dict__.pop("_state")
        if "basemodel_ptr_id" in data.__dict__:
            data.__dict__.pop("basemodel_ptr_id")
        if "id" in data.__dict__:
            data.__dict__.pop("id")
        target.append(data.__dict__)
    r["data"] = target
    log(r)
    return r


def buildjson(data):
    if isinstance(data, dict):
        r = build_result(SUCCESS, "success")
        r["data"] = data
        return r
    return build_result(SERVER_ERROR, SERVER_ERROR_MSG)
