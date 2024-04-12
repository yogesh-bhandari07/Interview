from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib.auth import authenticate
from .models import *



def home(request):
    products=Product.objects.all()
    return render(request,'products/index.html',{'products':products})

def productAdd(request):

    if request.method=="POST":
      
        name=request.POST.get('name')  
        price=request.POST.get('price')  
        description=request.POST.get('description')  
        product=Product.objects.create(name=name,price=price,description=description)
        product.save()
        return render(request,'products/add.html')
    
    elif request.method=="GET":
        return render(request,'products/add.html')

def productEdit(request,pk):
    if request.method=="POST":
        product=get_object_or_404(Product,id=pk)
        name=request.POST.get('name')  
        price=request.POST.get('price')  
        description=request.POST.get('description')  
        product.name=name
        product.price=price
        product.description=description
        product.save()
        return redirect('list_product')
    elif request.method=="GET":
        product=Product.objects.get(id=pk)
        return render(request,'products/edit.html',{'product':product})
    

def productDelete(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect('list_product')


def billing(request):
    products=Product.objects.all()
    return render(request,'billing/index.html',{'products':products})
