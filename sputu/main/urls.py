
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('announcements/', views.announcements, name='announcements'),
    path('contests/', views.contests, name='contests'),
    path('programs/', views.programs, name='programs'),
    path('contacts/', views.contacts, name='contacts'),
]