from django.urls import path
from .views import *


urlpatterns =[
    path('', index, name="index"),
    path('add/', add_phone, name="add_phone")
]