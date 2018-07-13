from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from host_test import models
def business(request):
    v = models.Business.objects.all()
    return render(request,'business.html',{'v':v})
