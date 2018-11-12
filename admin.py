from django.http import *
from django.shortcuts import render,redirect
from dataqueries import *

table = "admin"
database = "foodservice"

#opens up AdminSignin Page
def adminsigninpage(request):
    return render(request, 'admin/admingsignin.html')

def adminsigninaction(request):
    credentials = request.POST.get('signincredentials')
    password = request.POST.get('pwd')
    username = ""
    signupcomplete = False
    if('@' in credentials and '.' in credentials):
        data = password_valid(table,database,'password:'+password,'emailid:'+credentials)
        if(data):
            tmp = value_info(table,database,'username','emailid:'+credentials)
            if(tmp):
                username = tmp
    else:
        data = password_valid(table, database,'password:'+password,'username:' + credentials)
        username = credentials
    if(data):
        d = {}
        d['username'] = username
        return render(request,'admin/adminmain.html',{
            'info':d
        })

def adminforgetpasswordpage(request):
    return render(request, 'admin/adminforgetpassword.html')

def adminaddpage(request):
    return render(request,'admin/addadmin.html')

#def deleteadmin(request):

def adminview(request):

    message,data = selectall(table,database)
    sendlist = []
    if(data):
        for tuple in data:
            d = {}
            d['id'] = tuple[0]
            d['username'] = tuple[1]
            d['password'] = tuple[2]
            d['email'] = tuple[3]
            d['admintype'] = tuple[4]
            d['question'] = tuple[5]
            d['answer'] = tuple[6]
            sendlist.append(d)
    return render(request,'admin/viewadmin.html',{'data':sendlist})

def admindelete(request):
    username = request.POST.get('username')
    username = "'" + username + "'"
    try:
        message = delete(table,database,'username:'+username)
        return HttpResponseRedirect('adminview')
    except:
        return HttpResponseRedirect('adminview')

def adminaddaction(request):

    splitkey = "#+-+123-+-#"

    username = request.POST.get('username')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    admintype = request.POST.get('admintype')
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    values = username + splitkey + pwd + splitkey + email + splitkey + admintype + splitkey\
             + question + splitkey + answer

    user_exist = False
    colstr = 'username,emailid'
    if(username and email and pwd and admintype and question and answer):
        data = credentials_valid(table, database, colstr, [username, email])
        if (data):
            if(data[0] and data[1]):
                return HttpResponseRedirect('adminaddpage')
            else:
                try:
                    message = insert_into_table(table,database,values,splitkey)
                    return HttpResponseRedirect('adminview')
                except:

                    return HttpResponseRedirect('adminaddpage')
    return HttpResponseRedirect('adminaddpage')

def V_D(keystr,values):
    keylist = keystr.split(",")
    if(len(keylist) == len(values)):
        d = {}
        for a in range(0,len(values)):
            d[keylist[a]] = values[a]
        return d
    return None

def adminupdatepage(request):

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    admintype = request.POST.get('admintype')
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    values = [username,email,password,admintype,question,answer]
    keystr = "username,email,password,admintype,question,answer"
    data = V_D(keystr,values)
    if(data):

        return render(request, 'admin/updateadmin.html', {'data': data})

def adminupdateaction(request):
    splitkey = "++|,|++"            #this key is used to split data
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    admintype = request.POST.get('admintype')
    question = request.POST.get('question')
    answer = request.POST.get('answer')

    #username = "'" + username + "'"
    colstr = "username=" + username + splitkey + "emailid=" + email + splitkey + \
             "password=" + password + splitkey + "admintype=" + admintype + splitkey + \
             "securityquetion=" + question + splitkey + "answer=" + answer
    if (username and email and password and admintype and question and answer):
        data = update_table(table, database, "username:" +"'"+ username +"'", colstr, splitkey)
        return HttpResponseRedirect('adminview')

def cred(request):
    data = credentials_valid(table,database,'username,emailid',['Abh','abhi@gmail.com'])
    return HttpResponse(data)