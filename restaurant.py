from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from dataqueries import *
from conversions import *

table = 'restaurant'
database = 'foodservice'

def addrestaurentpage(request):
    message,citydata = selectall('city',database)
    if(citydata):
        cities = []
        for a in citydata:
            #if city is currently active then send the city name
            if(a[2].lower() == 'active'):
                d = {}
                d['cityid'] = a[0]
                d['cityname'] = a[1]
                d['status'] = a[2]
                cities.append(d)
        return render(request,'restaurant/addrestaurant.html',{'city':cities})

    return HttpResponse('There was a problem Getting the cities')

def viewrestaurentpage(request):

    error = False
    message, restaurantdata = selectall(table,database)
    message, citydata = selectall('city', database)
    restkeys = ['id','restaurantname','email','password','mobileno','address','ownername','city','status']
    citykeys = ['id','name','status']
    heads = ['Id','Restaurant Name','Email','Password','Mobileno','Address','Ownername','City','Status']

    if(restaurantdata and citydata):

        restlist = tuples_to_dictionaries(restaurantdata,restkeys)
        citydict = tuple_to_onekeydic(citydata)

        if(restlist and citydict):

            for index in range(0,len(restlist)):
                rowcityid = restlist[index]['city']

                if(rowcityid in citydict):
                    restlist[index]['city'] = citydict[rowcityid]

            return render(request,'restaurant/viewrestaurant.html',{
                'data':restlist,'heads':heads})

    return render(request,'restaurant/viewrestaurant.html')


def addrestaurentaction(request):
    restaurantname = request.POST.get('restaurantname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobileno = str(request.POST.get('mobileno'))
    address = request.POST.get('address')
    ownername = request.POST.get('ownername')
    city = request.POST.get('city')
    status = request.POST.get('status')

    if(restaurantname and email and password and mobileno and address and city and ownername and status):
        message,data = select(table,database,'email:'+email)
        if(not data):
            splitkey = "-+-+5123+-+"
            message,citydata = select('city',database,'cityname:'+city)
            cityid = str(citydata[0])
            valstr = restaurantname + splitkey + email + splitkey \
                     + password + splitkey + mobileno + splitkey + address \
                     + splitkey + ownername + splitkey + cityid + splitkey + status
            message = insert_into_table(table,database,valstr,splitkey)
            return HttpResponse(message)
        return HttpResponse('Same Email Found')


def deleterestaurentaction(request):
    restaurantid = request.POST.get('id')
    message = delete(table,database,'id:'+restaurantid)
    return HttpResponseRedirect('viewrestaurant')

def updaterestaurentpage(request):

    restaurantid = request.POST.get('id')
    message,restaurantdata = select(table,database,'id:'+restaurantid)
    keystr = 'id,restaurantname,email,password,mobileno,address,ownername,city,status'

    if(restaurantdata):
        restaurantcity = value_info('city', database, 'cityname', 'id:' + str(restaurantdata[7]))
        allcities = colum_data('city', database, 'cityname')

        if(restaurantcity and allcities):
            restdata = [a for a in restaurantdata]
            cityinfo = {}
            cityinfo['id'] = restdata[7]
            cityinfo['cityname'] = restaurantcity[0]
            #return HttpResponse(restaurantcity[0])
            restdata[7] = restaurantcity[0]
            senddata = T_TO_D(restdata,keystr)
            cities = L_IN_L_TO_L(allcities)
            #return HttpResponse(cities)

            if(senddata and cities):
                return render(request, 'restaurant/updaterestaurant.html',
            {'data':senddata,'cities':cities,'cityinfo':cityinfo})

    return HttpResponseRedirect('viewrestaurantpage')

def updaterestaurentaction(request):
    restaurantid = request.POST.get('id')
    restaurentname = request.POST.get('restaurantname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobileno = str(request.POST.get('mobileno'))
    address = request.POST.get('address')
    ownername = request.POST.get('ownername')
    city = request.POST.get('city')
    status = request.POST.get('status')

    cityiddata = value_info('city',database,'id','cityname:'+city)
    if(cityiddata):
        cityid = str(cityiddata[0])

    if (restaurentname and email and password and mobileno and address and cityid and ownername and status):
        splitkey = "+__52-+d+-31+-__+"
        valstr = 'restaurantname='+ restaurentname + splitkey + \
                 'email=' + email  + splitkey + 'password='+ password \
                 + splitkey + 'mobileno=' + mobileno + splitkey + 'address=' + address +splitkey\
                 + 'city='+ cityid +splitkey + 'ownername=' + ownername + splitkey \
                 + 'status=' + status
        message = update_table(table,database,'id:'+restaurantid,valstr,splitkey)
        return HttpResponseRedirect('viewrestaurant')
    else:
        return HttpResponse('All Data is mandatory')
    return HttpResponseRedirect('viewrestaurant')