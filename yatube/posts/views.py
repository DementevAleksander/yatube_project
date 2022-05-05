from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = 'posts\index.html'
    return render(request, template)


def group_posts(request, post):
    return HttpResponse(f'Пост: {post}')

def group_list(request):
    template = 'posts\group_list.html'
    return render(request, template)
