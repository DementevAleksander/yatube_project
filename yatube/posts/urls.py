# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:post>/', views.group_posts),
    path('group_list.html', views.group_list),
]