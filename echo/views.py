from django.shortcuts import render


def index(request):
    return render(request, 'echo/index.html')


def echo_image(request):
    return render(request, 'echo/echo_image.html')