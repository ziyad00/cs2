from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tour'
urlpatterns = [
  
    path('', views.tour, name='tour'),
    path('tour/<int:id>', views.teams, name='teams'),
]
