from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from login_home import models

def host_management(request):
    return render(request,"host_management.html")


