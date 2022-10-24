from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.shortcuts import render
from Esetup.emailbackend import EmailBackend

# Create your views here.
def loginpage(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method!= 'POST':
        return HttpResponse("<h1>Error 404</h1>")
    else:
        user= EmailBackend.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user!= None:
            login(request,user)
            return HttpResponse("Email :" + request.POST.get("email")+", Password :"+request.POST.get("password"))
        else:
            return HttpResponse("user does not exist")

def userdetails(request):
    if request.user != None:
        return HttpResponse("Username :" +request.user.email+"usertype :"+request.user.user_type)
    else:
        return HttpResponse("login first")
def dologout(request):
    logout(request)
    return HttpResponseRedirect("/")

