from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

from .models import *

def index(request):

    posts = Games.objects.all()

    context = {
        'menu': menu,
        'posts': posts,
        'title':'Главная страница',
        'cat_selected':0,
    }
    return render(request, 'games/index.html', context=context)

def show_category(request, cat_id):

    posts = Games.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404()

    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Записи по категории',
        'cat_selected': cat_id,
    }
    return render(request, 'games/index.html', context=context)


def about(request):
    return render(request, 'games/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Добавить статью')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизоваться')


def show_post(request, post_slug):
    post = get_object_or_404(Games, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'games/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ты криворукий</h1>')