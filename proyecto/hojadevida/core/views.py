from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def timer(request):
    return render(request, 'core/timer.html')
