from turtle import home
from django.urls import path,include
from django.contrib import admin
from.import views


urlpatterns = [
    path(r'^$',view= home,name= home),
]
