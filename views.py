from django.shortcuts import *
from django.http import *
from dataqueries import *
import string
def convert(request):
    a = int(request.GET['tb1'])
    b = int(request.GET['tb2'])

    c = a + b
    send = {}
    send['ans'] = c
    return JsonResponse(send)
pwd_necc_chars = []

def password_check(password):
    digits_true = False
    lowecase_true = False
    uppercase_true = False
    punctuations_true = False
    minlength_true = False
    maxlength_true = False
    space_at_ends = False

    min_length = 8
    max_length = 50
    password_length = 0

    ascii_lowercase = list(string.ascii_lowercase)
    ascii_uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuations = list(string.punctuation)
    whitespace = list(string.whitespace)
    printable = list(string.printable)
    index = 0

    error_message = ""
    for each in password:
        if (each in digits):
            digits_true = True

        if(each in ascii_lowercase):
            lowecase_true = True

        if(each in ascii_uppercase):
            uppercase_true = True

        if(each in punctuations):
            punctuations_true = True

        if(each in whitespace):
            if(index == 0 and index == len(password)):
                space_at_ends = True

        if (each in printable):
            password_length += 1

    if(password_length < min_length):
        minlength_true = True
    if(password_length > max_length):
        maxlength_true = True

    if(password_length == 0 ):
        error_message = "Enter Password"

    elif(minlength_true):
        if(maxlength_true):
            error_message = "Please use at least 8 characters and maximum 50 characters"
        else:
            error_message = "Please use at least 8 characters for password"

    elif(space_at_ends):
        error_message = "Whitespace should not be at starting and end of passwords"
    else:

        error_message = "Password should contain at least 1 "

        if not digits_true :
            error_message += " number"

        if not uppercase_true :
            if digits_true:
                error_message += " uppercase"
            else:
                error_message += " ,uppercase"

        if not lowecase_true:
            if digits_true and uppercase_true:
                error_message += " lowercase"
            else:
                error_message += " , lowercase"

        if not punctuations_true:
            if digits_true and uppercase_true and lowecase_true:
                error_message += " punctuations"
            else:
                error_message += " and punctuations"

        if digits_true and lowecase_true and uppercase_true and punctuations_true:
            error_message = ""


    return error_message

def email_check(email):


    if('@' in email):
        ''

    for each in email:
        ''

def validations(request):
    name = request.GET['name']
    password = request.GET['password']
    email = request.GET['email']

    if(password):
        pwd_err_msg = password_check(password)
    else:
        pwd_err_msg = "Enter Password"

    if(email):
       email_check(email)

    send = {}
    send['e-password'] = pwd_err_msg
    send['e-name'] = name + ' not evaluated yet'
    send['e-email'] = email + ' not evaluated yet'
    return JsonResponse(send)

def ajaxtesting(request):
    return render(request,'ajaxtesting.html')