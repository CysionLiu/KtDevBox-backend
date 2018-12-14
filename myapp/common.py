from datetime import datetime
from time import strftime

from django.db import models

from myapp.models import User
from myapp.tool import log


def build_result(code, msg):
    d = {"code": code, "msg": msg}
    return d


def build_model_data(data):
    r = build_result(200, "success")
    log(data.__dict__)
    if data.__dict__.has_key("createTime"):
        ct = data.__dict__.get("createTime")
        data.__dict__.pop("createTime")
        data.__dict__["createStamptime"] = ct.strftime('%Y-%m-%d %H:%M:%S')
    if data.__dict__.has_key("modifyTime"):
        mt = data.__dict__.get("modifyTime")
        data.__dict__.pop("modifyTime")
        data.__dict__["modifyStamptime"] = mt.strftime('%Y-%m-%d %H:%M:%S')
    if data.__dict__.has_key("_state"):
        data.__dict__.pop("_state")
    r["data"] = data.__dict__
    log(r)
    return r


def buildjson(data):
    if isinstance(data, dict):
        r = build_result(200, "success")
        r["data"] = data
        return r
    return build_result(500, "inner error")
