from django.shortcuts import render
from myblog.models import SiteInfo

# Create your views here.
def index(request):

    # logic
    # read and write data
    print("start write data....")
    siteInfo = SiteInfo.objects.all() #get all the data from siteinfo
    print(len(siteInfo))
    
    for item in siteInfo:
        print(item.title)
    data = {
        "siteinfo":siteInfo[0]
    }

    return render(request, 'index.html', data)