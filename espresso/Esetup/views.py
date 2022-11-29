from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from Esetup.emailbackend import EmailBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Esetup.models import CustomUser
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
                return HttpResponseRedirect('/studenthome')
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


# def temp(req):
#     return render(req, "base.html")

@login_required(login_url='/')
def userprofile(request):
    return render (request, 'profile.html')
@login_required(login_url='/')
def editprofile(request):
    user= CustomUser.objects.get(id= request.user.id)
    # print(user) 
    context= {
        "user":user,
    }
    return render(request, "editprofile.html", context)
@login_required(login_url='/')
def updateprofile(request):
    if request.method == "POST":
        profile_pic= request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        # email= request.POST.get('email')
        # username= request.POST.get('username')
        password= request.POST.get('password')
        # aboutme= request.POST.get('about')
        # print(profile_pic, first_name, last_name, password, email, username)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name= last_name
            # customuser.username = username
            # customuser.email = email
            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.display_pic = profile_pic
            customuser.save()
            messages.success(request, "Your profile updated successfully")
            # return render(request, "profile.html") 
            return redirect('user_profile')
            # used redirect to update image instantly, render failed to update the image
        except:
            messages.error(request, "Failed to update profile")
            return redirect(request, 'editprofile.html')
    # return HttpResponse("if didnt worked")