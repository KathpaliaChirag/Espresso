from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/') #used taki cookie ki wajha se logout baad login na ho as saved info
def adminhome(request):
    return render(request, "hod/hodbase.html")
