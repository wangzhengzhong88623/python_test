from django.shortcuts import redirect,HttpResponse
from django.shortcuts import render
from django.views import View
from host_test import models
def business(request):
    v = models.Business.objects.all()
    return render(request,'business.html',{'v':v})




def host(request):
    v1 = models.Host_test.objects.filter(nid__gt=0)
    for row in v1:
        print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,sep='\t')
    return render(request,'host.html',{'v1':v1})
