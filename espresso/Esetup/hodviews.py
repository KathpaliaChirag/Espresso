from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/') #used taki cookie ki wajha se logout baad login na ho as saved info
def adminhome(request):
    return render(request, "hod/hodbase.html")

@login_required(login_url='/')
def addstudent(request):
    return render(request, 'hod/addstudent.html')
@login_required(login_url='/')
def addstaff(request):
    return render(request, 'hod/addstaff.html')

@login_required(login_url= '/')
def addsubject(request):
    return render(request, 'hod/addsubject.html')

@login_required(login_url= '/')
def addcourse(request):
    return render(request, 'hod/addcourse.html')