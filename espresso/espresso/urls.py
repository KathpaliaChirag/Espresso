"""espresso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from Esetup import views, hodviews, staffviews, studentviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='loginpage'),
    path('dologin', views.dologin),
    path('usersdetails', views.userdetails),
    path('logout', views.dologout),
    # path('temp', views.temp),
#profie functions
    path('profile', views.userprofile, name= 'user_profile'),
    path('editprofile', views.editprofile, name= 'editprofile'),
    path('updateprofile', views.updateprofile, name= 'updateprofile'),
# admin functions
    path('adminhome', hodviews.adminhome, name= 'adminhome'),
    path('addstudent', hodviews.addstudent, name= 'addstudent'),
    path('addstaff', hodviews.addstaff, name= 'addstaff'),
    path('addsubject', hodviews.addsubject, name= 'addsubject'),
    path('addcourse', hodviews.addcourse, name= 'addcourse'),
    #student functions
    path('studenthome', studentviews.studenthome, name='studenthome'),

    #teacher function
    path('staffhome', staffviews.studenthome, name='staffhome'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)