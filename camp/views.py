from django.shortcuts import render, redirect

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Camp Index</h1>")
