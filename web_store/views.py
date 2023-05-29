from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

from web_store.models import Category,Product


# Create your views here.

def product(request):
    products = None # ตั้งตัวแปรมาก่อนไม่ให้มีค่าว่าง
    products = Product.objects.all().filter(available=True)  #ดึงข้อมูลจาก Productมา แล้ว กรองข้อมู available
    context = {'products':products}
    return render(request,'web_store/product.html',context) 