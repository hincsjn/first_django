from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def nya(request):
    return render(request, 'pages/nya.html')
