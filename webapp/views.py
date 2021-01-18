from django.shortcuts import render
from myapp.models import products_db,recipie_db,category_db
# Create your views here.
def home(request):
    # data1=category_db.objects.all()
    data=products_db.objects.all()
    data1=category_db.objects.all()
    return render(request,'home.html',{'data':data,'data1':data1})

def about(request):
    return render(request,'about.html')

def products(request):
    data=products_db.objects.all()
    print(data)
    return render(request,'products.html',{'data':data})

def recipes(request):
    data=recipie_db.objects.all()
    print(data)
    return render(request,'recipes.html',{'data':data})

def showrecipe(request,dataid):
    data=recipie_db.objects.filter(id=dataid)
    print(data)
    return render(request,'showrecipe.html',{'data':data})  

def myaccount(request):
    return render(request,'myaccount.html')

def register(request):
    return render(request,'register.html')

def mycart(request):
    return render(request,'mycart.html')