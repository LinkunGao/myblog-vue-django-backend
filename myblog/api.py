from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Courses, UserInfo
from myblog.toJson import Courses_data, UserInfo_data
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