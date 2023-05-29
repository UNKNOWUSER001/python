from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect

# Create your views here.

def home(request:HttpRequest):
    return render (request,'web_general/home.html')


def about(request:HttpRequest):
    return render(request,'web_general/about.html')
