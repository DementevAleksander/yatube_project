from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница yatube!')


def group_posts(request, post):
    return HttpResponse(f'Пост: {post}')
