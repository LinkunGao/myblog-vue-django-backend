from typing import overload
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from myblog import toJson
from myblog.models import Courses, SiteInfo, UserInfo
from myblog.toJson import Courses_data, UserInfo_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
import json

@api_view(['GET','POST'])
def apiTest(request):
    courses = Courses.objects.all()
    # crouses_data = Crouses_data(crouses, many=True)

    # users = UserInfo.objects.all()
    # users_data = UserInfo_data(users, many=True)

    # data = {
    #     'crouses':crouses_data.data,
    #     'users':users_data.data
    # }
    data = {
        'courses':[],
    }

    for course in courses:
        data_item = {
            'id':course.id,
            'text':course.text,
            'users':[]
        }
        users = course.userinfo_courses.all()
        for user in users:
            data_user = {
                'id':user.id,
                'nickName':user.nickName,
                'userIcon':str(user.icon)
            }
            data_item['users'].append(data_user)
        data['courses'].append(data_item)
    # data = json.dumps(data)

    return Response(data)

@api_view(['GET'])
def getMenuList(request):
    
    courses = Courses.objects.all()
    siteInfo = SiteInfo.objects.get(id=1)
    siteInfo_data = {
        'sitename':siteInfo.title,
        'icon':"http://127.0.0.1:9000/upload/"+str(siteInfo.icon)
    }
    #  整理数据为json
    menu_data = []
    for course in courses:
        data_item = {
            "id":course.id,
            "text":course.text
        }
        menu_data.append(data_item)
    data = {
        "menu_data":menu_data,
        "siteinfo":siteInfo_data
    }

    return Response(data)

@api_view(['GET','DELETE'])
def getUserList(request):
    if request.method == 'DELETE':
        user_id = request.POST['id']
        delete_user = UserInfo.objects.get(id=user_id)
        delete_user.delete()
        return Response('ok')
    menuId = request.GET['id']
    menu = Courses.objects.get(id=menuId)
    userlist = UserInfo.objects.filter(belong=menu)
    print(userlist)

    data = []
    for user in userlist:
        data_item = {
            'id':user.id,
            'nickName':user.nickName,
            'icon':str(user.icon)
        }
        data.append(data_item)
    return Response(data)

@api_view(['POST'])
def toLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    
    # 查询数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        auth_user = authenticate(username=username,password=password)
        if auth_user:
            token =  Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            userinfo = UserInfo.objects.get(belong_user=user[0])
            data = {
                'token':token.key,
                'userinfo':{
                    'id':userinfo.id,
                    'nickName':userinfo.nickName,
                    'icon':str(userinfo.icon),
                }
            }
            return Response(data)
        else:
            return Response("fail")
    else:
        return Response('none')

@api_view(['POST'])
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    # 判断用户
    user = User.objects.filter(username=username)
    if user:
        return Response('same_user')
    else:
        password = make_password(password,"azzsa")
        new_user = User(username=username, password=password)
        new_user.save()
    return Response('ok')

@api_view(['POST','PUT'])
def upload_icon(request):
    if request.method == 'PUT':
        webname = request.POST['webname']
        icon = request.POST['icon']
        old_website = SiteInfo.objects.get(id=1)
        old_website.title = webname
        new_site = SiteInfo.objects.get(id=2)
        old_website.icon = new_site.icon
        old_website.save()
        return Response('ok')
    img = request.FILES['icon']
    print(img)
    temp = SiteInfo.objects.get(id=2)
    temp.icon = img
    temp.save()
    data={
        'img':str(temp.icon)
    }
    return Response(data)
