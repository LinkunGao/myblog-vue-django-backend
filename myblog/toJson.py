from django.db import models
from rest_framework import serializers
from myblog.models import Crouses, UserInfo

class Crouses_data(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = Crouses
        fields = '__all__'

class UserInfo_data(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = UserInfo
        fields = '__all__'