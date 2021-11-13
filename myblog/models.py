from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(null=True,blank=True, max_length=50)
    icon = models.ImageField(upload_to='logo/', null=True, blank=True)
    
# pip install Pillow
    def __int__(self):
        return self.id