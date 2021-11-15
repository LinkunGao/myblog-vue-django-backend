from django.shortcuts import render, redirect
from myblog.models import SiteInfo,Courses,UserInfo
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):

    # basic info
    print("start write data....")
    siteInfo = SiteInfo.objects.all() #get all the data from siteinfo
    print(len(siteInfo))

    # menu
    courses = Courses.objects.all() 
    # userInfo
    users = UserInfo.objects.all()

    for item in siteInfo:
        print(item.title)
    data = {
        "siteinfo":siteInfo[0],
        "courses":courses,
        "users":users
    }
    
    return render(request, 'index.html', data)


def menu(request):
    # basic info

    siteInfo = SiteInfo.objects.all() #get all the data from siteinfo

    # menu
    courses = Courses.objects.all() 

    try:
        choosed_id = request.GET['id']
        choosed = Courses.objects.filter(id=choosed_id)
    except:
        return redirect('/')
    
    if choosed:
        users = UserInfo.objects.filter(belong=choosed[0])
    else:
        users = []

    data = {
        "siteinfo":siteInfo[0],
        "courses":courses,
        "users":users,
    }
    return render(request, 'menu.html',data)