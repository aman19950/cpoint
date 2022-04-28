from django.contrib import admin
from django.urls import path
from graphviz import view

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("save_info", views.save_information, name="save"),

]
