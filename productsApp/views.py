from django.shortcuts import render

from django.shortcuts import HttpResponse

def robot(request):
    html='<html><body>家用机器人</body></html>'
    return HttpResponse(html)

def monitoring(request):
    html='<html><body>显示器</body></html>'
    return HttpResponse(html)

def face(request):
    html='<html><body>面部识别</body></html>'
    return HttpResponse(html)