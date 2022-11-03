from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from Esetup.emailbackend import EmailBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Error 404</h1>")
    else:
        user = EmailBackend.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user != None:
            login(request, user)
            user_type= user.user_type
            if user_type == '1':
                return HttpResponseRedirect('/adminhome')
            elif user_type == '2':
                pass
            elif user_type == '3':
                pass
            else:
                messages.error(request, "Email and password are not identified")
                return render('loginpage')
            # return HttpResponse("Email :" + request.POST.get("email") + ", Password :" + request.POST.get("password"))
        else:
            messages.error( request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def userdetails(request):
    if request.user != None:
        return HttpResponse("Username :" + request.user.email + "usertype :" + request.user.user_type)
    else:
        return HttpResponse("login first")


def dologout(request):
    logout(request)
    return HttpResponseRedirect("/")


def temp(req):
    return render(req, "base.html")
