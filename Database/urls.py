"""Database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import *
from admin import *
from index import *
from restaurant import *
from cuisines import *
from city import *
from user import *


urlpatterns = [

    #main urls
    path('admin/', admin.site.urls),
    path('',indexpage,name='index'),

    #cuisine urls
    path('viewcuisines',viewcuisines,name='viewcuisines'),
    path('insertcuisinepage',insertcuisinepage,name='insertcuisinepage'),
    path('insertcuisineaction',insertcuisine,name='insertcuisineaction'),
    path('deletecuisine',deletecuisine,name='deletecuisine'),
    path('updatecusinepage',updatecuisinepage,name='updatecusinepage'),
    path('updatecuisineaction',updatecuisineaction,name='updatecusineaction'),

    #admin urls
    path('adminview',adminview,name='adminview'),
    path('adminaddpage',adminaddpage,name='adminaddpage'),
    path('addaction',adminaddaction,name='addadminaction'),
    path('signin',adminsigninpage,name='adminsigninpage'),
    path('signinaction',adminsigninaction,name='adminsigninaction'),
    path('forgetpassword',adminforgetpasswordpage,name='adminforgetpassword'),
    path('admindelete',admindelete,name='admindelete'),
    path('adminupdate',adminupdatepage,name='adminupdatepage'),
    path('adminupdateaction',adminupdateaction,name='adminupdateaction'),

    #restaurent urls
    path('addrestaurentpage',addrestaurentpage,name='addrestaurantpage'),
    path('addrestaurantaction',addrestaurentaction,name='addrestaurantaction'),
    path('viewrestaurant',viewrestaurentpage,name='viewrestaurant'),
    path('deleterestaurant',deleterestaurentaction,name='deleterestaurant'),
    path('updaterestaurantpage',updaterestaurentpage,name='updaterestaurantpage'),
    path('updaterestaurantaction',updaterestaurentaction,name='updaterestaurantaction'),

    #city urls
    path('addcity',addcitypage,name='addcitypage'),
    path('addcityaction',addcityaction,name='addcityaction'),
    path('viewcity',viewcity,name='viewcity'),
    path('updatecitypage',updatecitypage,name='updatecitypage'),
    path('updatecityaction',updatecityaction,name='updatecityaction'),
    path('deletecitypage', deletecitypage, name='deletecitypage'),
    path('deletecityaction', deletecityaction, name='deletecityaction'),

    #user urls
    path('usersignupaction',usersignupaction,name='usersignupaction'),
    path('usersignuppage',usersignuppage,name='usersignuppage'),
    path('viewuserpage',viewuserpage,name='viewuserpage'),
    path('deleteuser',deleteuser,name='deleteuser'),
    path('updateuserpage',updateuserpage,name='updateuserpage'),
    path('updateuseraction',updateuseraction,name='updateuseraction'),

    #check urls
    path('cred',cred),
    path('convert',convert),
    path('valid',validations,name='validations'),
    path('ajax',ajaxtesting,name='ajaxtesting'),
]
