from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from user.models import User
import csv

def get_user_info(users):
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

    return student_data


def get_user_stat():
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="")
    users = users.exclude(Application__app1__isnull=True)

    student_stat = dict()
    student_stat['all'] = users.count()
    student_stat['backends'] = users.filter(position='백엔드').count()
    student_stat['frontends'] = users.filter(position='프론트엔드').count()

    return student_stat


@staff_member_required
def Appview(request):
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="")
    users = users.exclude(Application__app1__isnull=True)

    student_data = get_user_info(users)
    student_stat = get_user_stat()
    context = {'student_data': student_data, 'student_stat': student_stat}

    return render(request, 'index.html', context)


@staff_member_required
def Backview(request):
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="").filter(position='백엔드')
    users = users.exclude(Application__app1__isnull=True)

    student_data = get_user_info(users)
    student_stat = get_user_stat()
    context = {'student_data': student_data, 'student_stat': student_stat}

    return render(request, 'index.html', context)


@staff_member_required
def Frontview(request):
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="").filter(position='프론트엔드')
    users = users.exclude(Application__app1__isnull=True)

    student_data = get_user_info(users)
    student_stat = get_user_stat()
    context = {'student_data': student_data, 'student_stat': student_stat}

    return render(request, 'index.html', context)

# 로컬 전용
def make_csv(request):
    #필요없는 유저 제거 연산
    users = User.objects.exclude(name="")
    users = users.exclude(Application__app1__isnull=True)

    # csv 파일에 쓸 데이터
    data = [['이름', '학번', '전공', '핸드폰 번호'], ]

    student_data = get_user_info(users)
    for student in student_data:
        st_list = list()
        st_list.append(student['name'])
        st_list.append(student['student_num'])
        st_list.append(student['major'])
        st_list.append(student['phone_num'])

        data.append(st_list)

    # 파일 쓰기 모드로 'data.csv' 파일을 열고 csv writer 객체 생성
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

    return None