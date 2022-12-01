# _________________________________________________________________________________________________________________________
# removed name email password from the  sttudent, admin and hod to normalize into 1 (django custom user takes this info already)
# _______________________________________________________________________________________________________________
# from email.policy import default
# from pyexpat import model
# from tkinter import CASCADE
# from email.policy import default
from django.db.models.signals import post_save
# from django.dispatch import receiver
from secrets import choice
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_data = ((1, "Hod"), (2, "staff"), (3, "student"))
    user_type = models.CharField(default=1, choices=user_data, max_length=10)
    # gender_data = ((1, "Male"), (2, "Female"))
    # user_gender = models.CharField(default = 1, choices= gender_data, max_length= 10)
    # user_address= models.CharField(default ="Not defined", max_length= 300)
    display_pic= models.ImageField(default= "", upload_to='displaypic')


# Create your models here.
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,
                                 on_delete=models.CASCADE)  # one to one model between user and hod and same again one to onr for student/staff with user
    # name = models.CharField(max_length= 255)
    # email = models.CharField(max_length= 255)
    # password = models.CharField(max_length= 255)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    object = models.Manager()




class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = models.Manager()

    def __str__(self):
        return self.course_name

class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    Department_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = models.Manager()

    def __str__(self):
        return self.course_name

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    session_start = models.CharField(max_length=255)
    session_end = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = models.Manager()

    def __str__(self):
        a= self.session_start + "-" + self.session_end
        return a

class staff(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender= models.CharField(max_length=255)
    mobile= models.CharField(max_length=10)
    # name = models.CharField(max_length= 255)
    # email = models.CharField(max_length= 255)
    # password = models.CharField(max_length= 255)
    address = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    object = models.Manager()

def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name


class students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    # session_start_year = models.DateField()
    # session_end_year = models.DateField()
    # name = models.CharField(max_length= 255)
    # email = models.CharField(max_length= 255)
    # password = models.CharField(max_length= 255)
    # dp = models.FileField()
    # session_id = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    # object= models.Manager()

    def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name


class subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subjects_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    object = models.Manager()


class attendence(models.Model):
    id = models.AutoField(primary_key=True)
    Student_id = models.ForeignKey(students, on_delete=models.DO_NOTHING)
    attendence_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class AttendanceStatus(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students, on_delete=models.DO_NOTHING)
    attendence_id = models.ForeignKey(attendence, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class LeaveReportstudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_reason = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class LeaveReportstaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_reason = models.TextField()
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class LiabraryBook(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    publication_name = models.CharField(max_length=255)
    Author_name = models.CharField(max_length=255)
    purchased_on = models.DateTimeField(blank=True)
    book_status = models.BooleanField(default=False)
    object = models.Manager()


class Issuedstatusstudent(models.Model):
    issue_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students, on_delete=models.CASCADE)
    issue_date = models.CharField(max_length=255)
    return_date = models.CharField(max_length=255)
    issue_status = models.BooleanField(default=False)
    objects = models.Manager()


class Issuedstatusstaff(models.Model):
    issue_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    issue_date = models.CharField(max_length=255)
    return_date = models.CharField(max_length=255)
    issue_status = models.BooleanField(default=False)
    objects = models.Manager()


class studentFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class staffFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()


class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    objects = models.Manager()

#signals below
# @receiver(post_save, sender=CustomUser) #this will auto send account to the section as per admin id when we create
# def create_user_profile(sender, instance, created, **kwargs):
#     if created: #data is sent as input
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type == 2:
#             staff.objects.create(admin=instance)
#         if instance.user_type == 3:
#             students.objects.create(admin=instance)


# @receiver(post_save, sender=CustomUser)# this will save data
# def create_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.AdminHOD.save()
#     if instance.user_type == 2:
#         instance.staff.save()
#     if instance.user_type == 3:
#         instance.students.save()
