from django.shortcuts import redirect,HttpResponse
from django.shortcuts import render
from django.views import View
from host_test import models
def business(request):
    v = models.Business.objects.all()
    return render(request,'business.html',{'v':v})




def host(request):
    v1 = models.Host_test.objects.filter(nid__gt=0)#过滤条件nid大于0得
    v2 = models.Host_test.objects.filter(nid__gt=0).values('nid','hostname','ip','port','b__caption','b__code')
    v3 = models.Host_test.objects.filter(nid__gt=0).values_list('nid','hostname','ip','port','b__caption','b__code')
    print ("--------------------------------打印v1")
    print (v1)
    for row in v1:
        if row.hostname == "wangzzhost":
            print (row.hostname)
    print ()
    print ("--------------------------------打印v2")
    print (v2)
    for row in v2:
        if row["hostname"] == "wangzzhost":
            print (row['hostname'])
    print ()
    print ("--------------------------------打印v2")
    print (v3)
    for row in v3:
        if row[1] == "wangzzhost":
            print (row[1])
    print ()
    #for row in v1:
    #    print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,sep='\t')
    return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3})
