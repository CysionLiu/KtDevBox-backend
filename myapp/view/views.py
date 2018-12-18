import base64
import hashlib
import random
import time

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp import common
from myapp.models import *
import re
from django.core import paginator
# Create your views here.
from myapp.tool import log


def index(request):
    d = {"name": "welcome"}
    return JsonResponse(d)

def add_looper(request):
    if request.method == 'POST':
        params = request.POST
        if "type" not in params or "mediaId" not in params:
            return JsonResponse(common.build_result(400, "lack param"), safe=False)
        r_type = request.POST.get("type", '0')
        r_id = request.POST.get("mediaId", '1')
        r_link = request.POST.get("link", '0')
        r_title = request.POST.get("title", 'title')
        r_pic = request.POST.get("picUrl", '0')
        tmp = Looper(type=r_type, mediaId=r_id, link=r_link, title=r_title, picUrl=r_pic)
        tmp.save()
        return JsonResponse(common.build_result(200, "success"))
    return JsonResponse(common.build_result(400, "error http method"), safe=False)


def get_looper(request):
    cr = Looper.objects.all()
    return JsonResponse(common.build_model_list(cr), safe=False)
