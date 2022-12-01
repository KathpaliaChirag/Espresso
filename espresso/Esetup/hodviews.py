from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Esetup.models import Courses, Session, CustomUser, students
from django.contrib import messages


# used taki cookie ki wajha se logout baad login na ho as saved info
@login_required(login_url='/')
def adminhome(request):
    return render(request, "hod/hodbase.html")


@login_required(login_url='/')
def addstudent(request):
    course = Courses.object.all()
    session = Session.object.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password_var = request.POST.get('password')
        gender_var = request.POST.get('gender')
        course_selected = request.POST.get('course')
        # session_selected = request.POST.get('session')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "email exists for another user")
            return redirect('addstudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "email exists for another user")
            return redirect('addstudent')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                # password= password,
                display_pic=profile_pic,
                user_type=3
            )

            user.set_password(password_var)
            user.save()

            course_var = Courses.object.get(id=course_selected)
            # session_var = Session.object.get(id=session_selected)

            student = students(
                admin=user,
                address=address,
                # session_id = session_var,
                course_id=course_var,
                gender=gender_var
            )

            # print('accessing student model')
            student.save()
            messages.success(request, 'Successfully added student')
            return redirect("addstudent")

        # print(address, session, password, course)

    context = {
        "course": course,
        'session': session,
    }
    return render(request, 'hod/addstudent.html', context)


@login_required(login_url='/')
def addstaff(request):
    course= Courses.object.all()
    context = {
        'course': course
    }
    return render(request, 'hod/addstaff.html', context)


@login_required(login_url='/')
def addsubject(request):
    return render(request, 'hod/addsubject.html')


@login_required(login_url='/')
def addcourse(request):
    return render(request, 'hod/addcourse.html')
