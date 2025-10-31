from django.shortcuts import render
from django.shortcuts import HttpResponse
def home(request):
 return render(request,'home.html',{'active_menu':'home'})
# Create your views here.
