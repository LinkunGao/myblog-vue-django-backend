from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(null=True,blank=True, max_length=50)
    icon = models.ImageField(upload_to='logo/', null=True, blank=True)

# pip install Pillow
    def __int__(self):
        return self.id

# crouse categories
class Crouses(models.Model):
    text = models.CharField(null=True,blank=True, max_length=50)
    def __str__(self):
        return self.text

# users
class UserInfo(models.Model):
    nickName = models.CharField(null=True,blank=True, max_length=50)
    icon = models.ImageField(upload_to='user_icon/', null=True, blank=True)
    belong = models.ForeignKey(Crouses, on_delete=models.SET_NULL, related_name="userinfo_crouses", null=True, blank=True)

    def __str__(self):
        return self.nickName