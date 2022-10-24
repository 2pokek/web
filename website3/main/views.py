from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def asd(request):
    return HttpResponse("<h1>ASD</h1>")


def main(request):
    return render(request,'Main.html')
