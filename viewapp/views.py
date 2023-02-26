from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from user.models import User
# from application.models import Application

@staff_member_required
def Appview(request):
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="")
    users = users.exclude(Application__app1__isnull=True)

    student_data = list()
    for user in users:
        student = dict()
        student['name'] = user.name
        student['major'] = user.major
        student['student_num'] = user.student_num
        student['semester'] = user.semester
        student['created_at'] = user.created_at
        student['phone_num'] = user.phone_num
        student['position'] = user.position
        student['id'] = user.id
        student['github'] = user.Application.github
        student['app1'] = user.Application.app1
        student['app2'] = user.Application.app2
        student['app3'] = user.Application.app3
        student['app4'] = user.Application.app4
        student_data.append(student)
    
    context = {'student_data': student_data}

    return render(request, 'index.html', context)