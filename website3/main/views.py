from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-last_modified')
    return render(request, 'index.html', {'title': 'Главная страница', 'tasks': tasks})


def hacks(request):
    return render(request, 'hacks.html')


def asd(request):
    return HttpResponse("<h1>ASD</h1>")


def main(request):
    return render(request, 'Main.html')
def create(request):
    return render(request, 'create.html')

