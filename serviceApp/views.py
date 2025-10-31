from django.shortcuts import render

from django.shortcuts import HttpResponse

def download(request):
    html='<html><body>资料下载</body></html>'
    return HttpResponse(html)

def platform(request):
    html='<html><body>开放平台</body></html>'
    return HttpResponse(html)

