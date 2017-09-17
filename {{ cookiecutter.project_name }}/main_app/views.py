# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'main_app/index.html')
