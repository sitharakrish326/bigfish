from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from .models import admins_db,products_db,recipie_db,category_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def my(request):
    return render(request,'base.html')

def addadmin(request):
    return render(request,'addadmin.html')

def admindatas(request):
    data = dict()
    if request.method == 'POST':
        name_r=request.POST.get('name')
        username_r=request.POST.get('username')
        password_r= request.POST.get('password')
        image_r=request.FILES['file']
        if admins_db.objects.filter(username=username_r).exists():
            data['error']=0
            data['message']="username already exists"
            return JsonResponse(data)
        if admins_db.objects.filter(password=password_r).exists():
            data['error']=0
            data['message']="username already exists"
            return JsonResponse(data)
        obj=admins_db(name=name_r,username=username_r,password=password_r,image=image_r)
        obj.save()
        data['message']="Succesfully Registered"
        data['error']=1
        return JsonResponse(data)
        
def viewadmins(request):
    data=admins_db.objects.all()
    return render(request,'viewadmins.html',{"data":data})

def deleteadmins(request,dataid):
        admins_db.objects.filter(id=dataid).delete()
        return redirect('viewadmins')

def editadmin(request,dataid):
    data=admins_db.objects.filter(id=dataid)
    return render(request, 'editadmin.html', {'data':data} )

def updateadmin(request,dataid):
    data=dict()
    if request.method == 'POST':
        name_r=request.POST.get('name')
        username_r=request.POST.get('username')
        password_r= request.POST.get('password')
        try:
            image_r=request.FILES['file']
            fs = FileSystemStorage() 
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError :
            file=admins_db.objects.get(id=dataid).image
        admins_db.objects.filter(id=dataid).update(name=name_r,username=username_r,password=password_r,image=file)

def addproduct(request):
    # data=products_db.objects.all()
    return render(request,'addproduct.html')

def productdatas(request):
    if request.method == 'POST':
        name_r=request.POST.get('name')
        weight_r=request.POST.get('weight')
        price_r= request.POST.get('price')
        image_r=request.FILES['file1']
        obj=products_db(name=name_r,weight=weight_r,price=price_r,image=image_r)
        obj.save()
        print(obj)
        
        return redirect('addadmin')

def viewproducts(request):
    data=products_db.objects.all()
    print(data)
    return render(request,'viewproducts.html',{"data":data})

def deleteproducts(request):
    if request.method == 'POST':
        dataid            = request.POST.get('data_id')
        products_db.objects.filter(id=dataid).delete()
        return redirect('viewproducts')

def editproducts(request,dataid):
    data=products_db.objects.filter(id=dataid)
    return render(request,'editproduct.html',{'data':data}) 

def updateproducts(request,dataid):
    if request.method == 'POST':
        name_r=request.POST.get('name')
        weight_r=request.POST.get('weight')
        price_r= request.POST.get('price')
        try:
            image_r=request.FILES['file1']
            fs = FileSystemStorage() 
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError :
            file=products_db.objects.get(id=dataid).image
        products_db.objects.filter(id=dataid).update(name=name_r,weight=weight_r,price=price_r,image=file)
        return redirect('viewproducts')

def addrecipies(request):
    return render(request,'addrecipies.html')

def recipiedatas(request):
    if request.method == 'POST':
        recipiename_r=request.POST.get('recipiename')
        ingredients_r=request.POST.get('ingredients')
        instructions_r= request.POST.get('instructions')
        image_r=request.FILES['file1']
        obj=recipie_db(recipiename=recipiename_r,ingredients=ingredients_r,instructions=instructions_r,image=image_r)
        obj.save()
        print(obj)
        return redirect('addrecipies')

def viewrecipies(request):
    data=recipie_db.objects.all()
    return render(request,'viewrecipies.html',{"data":data})

def deleterecipies(request):
    if request.method == 'POST':
        dataid            = request.POST.get('data_id')
        recipie_db.objects.filter(id=dataid).delete()
        return redirect('viewrecipies')

def editrecipies(request,dataid):
    data=recipie_db.objects.filter(id=dataid)
    return render(request,'editrecipie.html',{'data':data})

def updaterecipies(request,dataid):
    recipiename_r=request.POST.get('recipiename')
    ingredients_r=request.POST.get('ingredients')
    instructions_r= request.POST.get('instructions')
    try:
        image_r=request.FILES['file1']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=recipie_db.objects.get(id=dataid).image
    recipie_db.objects.filter(id=dataid).update(recipiename=recipiename_r,ingredients=ingredients_r,instructions=instructions_r,image=file)
    return redirect('viewrecipies')

def customers(request):
    return render(request,'customers.html')

def cart(request):
    return render(request,'cart.html')

def categorydescription(request):
    return render(request,'addcategories.html')

def categorydatas(request):
    data=dict()
    if request.method == 'POST':
        catname=request.POST.get('cname')
        catdesc=request.POST.get('cdescription')
        image_r=request.FILES['file']
        obj=category_db(cname=catname,catdescpn=catdesc,image=image_r)
        obj.save()
        data['message']="Succesfully Registered"
        data['error']=1
        return JsonResponse(data)

def viewcategory(request):
    data=category_db.objects.all()
    return render(request,'viewcategories.html',{"data":data})

def deletecategory(request,dataid):
        category_db.objects.filter(id=dataid).delete()
        return redirect('viewcategory')

def editcategory(request,dataid):
    data=category_db.objects.filter(id=dataid)
    return render(request,'editcategory.html',{'data':data})

def updatecategory(request,dataid):
    cname_r=request.POST.get('cname')
    desc_r=request.POST.get('cdescription')
    try:
        image_r=request.FILES['file']
        fs = FileSystemStorage() 
        file = fs.save(image_r.name, image_r)
    except MultiValueDictKeyError :
        file=category_db.objects.get(id=dataid).image
    category_db.objects.filter(id=dataid).update(cname=cname_r,catdescpn=desc_r,image=file)
    return redirect('viewcategory')