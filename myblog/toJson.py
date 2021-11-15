from django.db import models
from rest_framework import serializers
from myblog.models import Courses, UserInfo

class Courses_data(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = Courses
        fields = '__all__'

class UserInfo_data(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = UserInfo
        fields = '__all__'