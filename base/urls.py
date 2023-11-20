from base.views import index
from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index),
    path('create_camp/', create_camp, name='create_camp')
]
