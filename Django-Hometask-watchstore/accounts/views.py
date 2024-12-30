#usere web uzerinden httpresponse qaytaririq
from django.shortcuts import render

from django.http import HttpResponse

def say_hi(request): #request-funksiyanin ilk arqumenti olur.Django-da istifadəçidən serverə gələn HTTP sorğusunun bütün məlumatlarını ozunde saxlayan bir obyekt
    return HttpResponse("Hello, world!") #server istifadəçiyə cavab verir