from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(Request):
    #  return HttpResponse("<h1>Hello! all this is my first Django app</h1>")
    my_dict = {'insert_me': "I am coming from subfolder app1_home/reg.html"}
    return render(Request,'app1_home/registration.html',context=my_dict)