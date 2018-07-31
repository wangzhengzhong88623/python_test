from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from login_home import models

def service_line_management(request):
    return render(request,"service_line_management.html")
