from django.contrib import admin
from Esetup.models import CustomUser, Courses, Session, students
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    pass 
admin.site.register(CustomUser)
admin.site.register(Courses)
admin.site.register(Session)
admin.site.register(students)