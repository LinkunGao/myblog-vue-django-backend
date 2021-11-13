from django.contrib import admin
from myblog.models import SiteInfo, Crouses, UserInfo

# Register your models here.
admin.site.register(SiteInfo)
admin.site.register(Crouses)
admin.site.register(UserInfo)