from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,Alexander! You're at the mysite index.")
