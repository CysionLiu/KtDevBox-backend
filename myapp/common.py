import base64
import time
from datetime import datetime
from time import strftime

from django.db import models

from myapp.models import User
from myapp.tool import log

def create_token(uid,pwd,type):
    curtime = int(round(time.time() * 1000))
    itoken = base64.b64encode(("%s;%s;%s;%d" % (uid, pwd, type,curtime)).encode("utf-8"))
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
        target.append(data.__dict__)
    r["data"] = target
    log(r)
    return r


def buildjson(data):
    if isinstance(data, dict):
        r = build_result(200, "success")
        r["data"] = data
        return r
    return build_result(500, "inner error")
