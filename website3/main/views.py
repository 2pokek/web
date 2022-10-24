from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'index.html')


def hacks(request):
    return render(request, 'hacks.html')


def asd(request):
    return HttpResponse("<h1>ASD</h1>")


def main(request):
    return render(request, 'Main.html')
