from django.urls import path
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.questions, name = 'questions'),
    path('updatestats', views.UpdateStats, name='update_stats'),
    path('viewuserstats', views.ViewUserStats.as_view(), name = "stats_display"),
    path('register', views.UserCreateView.as_view(), name = "create_user"),
    path('logout', views.LogoutView, name = 'logout_view'),
    path('leaderboard', views.LeaderBoardView, name = 'leaderboard_view'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
