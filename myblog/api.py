from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Crouses, UserInfo
from myblog.toJson import Crouses_data, UserInfo_data
import json

@api_view(['GET','POST'])
def apiTest(request):
    crouses = Crouses.objects.all()
    # crouses_data = Crouses_data(crouses, many=True)

    # users = UserInfo.objects.all()
    # users_data = UserInfo_data(users, many=True)

    # data = {
    #     'crouses':crouses_data.data,
    #     'users':users_data.data
    # }
    data = {
        'crouses':[],
    }

    for crouse in crouses:
        data_item = {
            'id':crouse.id,
            'text':crouse.text,
            'users':[]
        }
        users = crouse.userinfo_crouses.all()
        for user in users:
            data_user = {
                'id':user.id,
                'nickName':user.nickName,
                'userIcon':str(user.icon)
            }
            data_item['users'].append(data_user)
        data['crouses'].append(data_item)
    # data = json.dumps(data)

    return Response(data)