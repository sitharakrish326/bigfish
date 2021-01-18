from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('recipes/',views.recipes,name='recipes'),
    path('showrecipe/<int:dataid>',views.showrecipe,name='showrecipe'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('register/',views.register,name='register'),
    path('mycart/',views.mycart,name='mycart'),
]