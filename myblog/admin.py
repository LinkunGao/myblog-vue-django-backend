from django.contrib import admin
from myblog.models import SiteInfo, Courses, UserInfo

# Register your models here.
admin.site.register(SiteInfo)
admin.site.register(Courses)
admin.site.register(UserInfo)