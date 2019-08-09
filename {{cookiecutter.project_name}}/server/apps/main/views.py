# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'main/index.html')
