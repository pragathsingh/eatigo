from django.http import *
from django.shortcuts import *
from dataqueries import *
import os
from conversions import *

image_upload_path = 'static/uploads/users/'
table = 'user'
database = 'foodservice'

def write_image(photo,photopath):
    photoname = str(photo)
    if not os.path.exists(photopath):
        os.mkdir(photopath)

    with open(photopath+"/"+photoname, 'wb+') as destination:
        for chunk in photo.chunks():
            destination.write(chunk)


def usersignuppage(request):

    cities = ['Amritsar','Jalandhar','Chandigarh','Jaipur','Ludhiana','Patiala','Bhatinda','Batala','Firozpur']
    cities.sort()
    return render(request,'user/usersignup.html',{'cities':cities})

def viewuserpage(request):
    message,data = selectall(table,database)
    keys = ['id','name','email','password','mobileno','address','photo','city']
    heads = []
    for a in keys:
        heads.append(a.capitalize())

    if(len(data) > 0):
        dataindic =  tuples_to_dictionaries(data,keys)
        if(len(dataindic) > 0):
            return render(request,'user/viewuser.html',{'data':dataindic,'heads':heads,'userfound':True})
    message = "There wasn't any User found in Database"
    return render(request, 'user/viewuser.html', {'heads': heads,'message':message,'userfound':False})


def usersignupaction(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobileno = str(request.POST.get('mobileno'))
    address = request.POST.get('address')
    city = request.POST.get('city')
    try:
        photo = request.FILES['photo']
    except:
        photo = None

    splitkey = '++--+123+--++'
    if(email and photo):
        photolocation = image_upload_path + email
        write_image(photo,photolocation)
        photolocation = photolocation[7:] + "/" + str(photo)

    if(photo == None):
        photolocation = 'None'

    if(username and email and password and mobileno and address and city):
        #return HttpResponse('all')

        values = username + splitkey + email + splitkey + password + splitkey + mobileno \
                     + splitkey + address + splitkey + photolocation + splitkey + city

        message,data = select(table,database,'email:'+email)
        if(data == None):
            message = insert_into_table(table,database,values,splitkey)
            return HttpResponseRedirect('viewuserpage')

    return HttpResponseRedirect('usersignuppage')

def deleteuser(request):
    userid = request.POST.get('id')
    message = delete(table,database,'id:'+userid)

    return HttpResponseRedirect('viewuserpage')

def updateuserpage(request):
    id = request.POST.get('id')
    message,userdata = select(table,database,'id:'+id)
    keys = ['id','name','email','password','mobileno','address','photo','city']
    cities = ['Amritsar', 'Jalandhar', 'Chandigarh', 'Jaipur', 'Ludhiana', 'Patiala', 'Bhatinda', 'Batala', 'Firozpur']
    cities.sort()
    #return HttpResponse(userdata)
    if(userdata):
        userlist = make_dictionary(keys,userdata)
        return render(request,'user/updateuser.html',{'user':userlist,'cities':cities})


def updateuseraction(request):
    id = request.POST.get('id')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobileno = str(request.POST.get('mobileno'))
    address = request.POST.get('address')
    city = request.POST.get('city')
    try:
        photo = request.FILES['photo']
    except:
        photo = None

    splitkey = '++--+123+--++'
    if (email and photo):
        photolocation = image_upload_path + email
        write_image(photo, photolocation)
        photolocation = photolocation[7:] + "/" + str(photo)

    if (username and email and password and mobileno and address and city):

        if(photo):
            valstr = 'name=' + username + splitkey + 'email=' + email + splitkey \
                     + 'password=' + password + splitkey + 'mobileno=' + mobileno \
                     + splitkey + 'address=' + address + splitkey + 'photo=' + photolocation \
                     + splitkey + 'city=' + city
        else:
            valstr = 'name=' + username + splitkey + 'email=' + email + splitkey \
                 + 'password=' + password + splitkey + 'mobileno=' + mobileno  \
                 + splitkey + 'address=' + address + splitkey + 'city=' + city

        message = update_table(table,database,'id:'+id,valstr,splitkey)
        return HttpResponseRedirect('viewuserpage')
