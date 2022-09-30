from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
               'posts': posts,
    }
    return render(request, template, context)
#    return HttpResponse('Главная страница')

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет храниться информация о группах проекта yatube'
    context = {
               'title': title,
    }
    return render(request, template, context)
#    return HttpResponse(f'Список сообществ {slug}')