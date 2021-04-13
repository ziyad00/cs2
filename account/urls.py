from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  
    path('user/', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
   # path('tour/', views.tour, name='tour'),
    #path('teams/', views.teams, name='teams'),


]
