from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)
#    return HttpResponse('Главная страница')

def group_posts(request, slug):
    template = 'posts/group'
    return render(request, template)
#    return HttpResponse(f'Список сообществ {slug}')