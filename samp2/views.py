
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
  return HttpResponse('<h1 align="center">"WELCOME TO INDEX PAGE"</h1><img src="https://cdn.pixabay.com/photo/2019/11/02/20/18/fog-4597348_960_720.jpg" height="100%" width="100%">')

def home(request):
  return render(request,"home.html")

def western(request):
  return render(request,"western.html")

def contact(request):
  return render(request,"contact.html")