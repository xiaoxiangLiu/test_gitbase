# coding=utf-8
from django.shortcuts import render

# Create your views here.

def index(request):
    list = [1, 2, 3, 4, 5, 6]
    return render(request, 'home.html', {'list': list})
