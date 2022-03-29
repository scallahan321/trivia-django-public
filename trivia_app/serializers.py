from wsgiref import validate
from rest_framework import serializers
from .models import User, Stats
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class ViewStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ['user_ref', 'questions_attempted', 'correct_answers', 'cat9_attempted', 'cat9_correct', 'cat10_attempted',
                 'cat10_correct', 'cat11_attempted', 'cat11_correct', 'cat12_attempted', 'cat12_correct', 'cat14_attempted',
                 'cat14_correct', 'cat15_attempted', 'cat15_correct', 'cat17_attempted', 'cat17_correct', 'cat21_attempted',
                 'cat21_correct', 'cat22_attempted', 'cat22_correct', 'cat23_attempted', 'cat23_correct'
                ]
