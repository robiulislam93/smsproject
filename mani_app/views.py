from django.shortcuts import render,HttpResponse
from .models import Univesity
from .froms import *
# Create your views here.
def show_uni(request):
    u=Univesity.objects.all()
    context={'university':u}
    return render (request,'apptem/univeisty.html',context)

def  add_product (request):
    if request.method == "POST":
        form= AddProduct (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Done")
    form= AddProduct()
    context = {'form':form}
    return render (request,'apptem/add_product.html',context)