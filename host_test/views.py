from django.shortcuts import redirect,HttpResponse
from django.shortcuts import render
from django.views import View
from host_test import models
import json,pdb
def business(request):
    v = models.Business.objects.all()
    return render(request,'business.html',{'v':v})


def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('bid')
        print (h,i,p,b)
        print (len(h))
        if h and len(h) > 5:
            pdb.set_trace()
            models.Host_test.objects.create(hostname=h,
                                           ip=i,
                                           port=p,
                                           b_id=b)
        else:
            ret['status'] = False
            ret['error'] = "太短了"
    except Exception as e:
         ret['status'] = False
         ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))

def host(request):
   # v1 = models.Host_test.objects.filter(nid__gt=0)#过滤条件nid大于0得
   # v2 = models.Host_test.objects.filter(nid__gt=0).values('nid','hostname','ip','port','b__caption','b__code')
   # v3 = models.Host_test.objects.filter(nid__gt=0).values_list('nid','hostname','ip','port','b__caption','b__code')
   # print ("--------------------------------打印v1")
   # print (v1)
   # for row in v1:
   #     if row.hostname == "wangzzhost":
   #         print (row.hostname)
   # print ()
   # print ("--------------------------------打印v2")
   # print (v2)
   # for row in v2:
   #     if row["hostname"] == "wangzzhost":
   #         print (row['hostname'])
   # print ()
   # print ("--------------------------------打印v2")
   # print (v3)
   # for row in v3:
   #     if row[1] == "wangzzhost":
   #         print (row[1])
   # print ()
   # #for row in v1:
   # #    print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,sep='\t')
    if request.method == "GET":
       v1 = models.Host_test.objects.filter(nid__gt=0)#过滤条件nid大于0得
       v2 = models.Host_test.objects.filter(nid__gt=0).values('nid','hostname','ip','port','b__caption','b__code')
       v3 = models.Host_test.objects.filter(nid__gt=0).values_list('nid','hostname','ip','port','b__caption','b__code')
       b_list = models.Business.objects.all() 
       return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3,'b_list':b_list})
    elif request.method == "POST":
       h = request.POST.get('hostname')
       i = request.POST.get('ip')
       p = request.POST.get('port')
       b = request.POST.get('bid')
       print (h,i,p,b)
       models.Host_test.objects.create(hostname = h,ip = i,port = p,b_id = b)
       return redirect('/host')

