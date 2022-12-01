from django.contrib import admin
from Esetup.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    pass 
admin.site.register(CustomUser)
admin.site.register(Courses)
admin.site.register(Session)
admin.site.register(students)
admin.site.register(Departments)