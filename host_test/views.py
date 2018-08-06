from django.shortcuts import redirect,HttpResponse
from django.shortcuts import render
from django.views import View
from host_test import models
from django.utils.safestring import mark_safe
import json,pdb
def business(request):
    v = models.Business.objects.all()
    return render(request,'business.html',{'v':v})

#--------------------------------------------------------------------
def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        host = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('bid')
        print (host,i,p,b)
        print (len(host))
        if host and len(host) > 5:
            models.Host_test.objects.create(hostname=host,
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

from django.core.handlers.wsgi import WSGIRequest
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
    print(type(request))
    print(request.environ)
    print(request.environ['HTTP_USER_AGENT'])
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
       models.Host_test.objects.create(hostname = h,ip = i,port = p,b_id = b)
       return redirect('/host')
def edit_host():
    pass
#-------------------------------------------------------------
def test_app(request):
     if request.method == "GET":
         app_list = models.Application.objects.all()
         host_list = models.Host_test.objects.all()
         return render(request,'app.html',{"app_list":app_list,"host_list":host_list})
     elif request.method == "POST":
         app_name = request.POST.get('app_name')
         host_list = request.POST.getlist('host_list')
         print (app_name,host_list)
         obj = models.Application.objects.create(name=app_name)
         obj.r.add(*host_list)
         return redirect('/test_app')
def ajax_add_app(request):
         ret = {'status':True,'error':None,'data':None}
         app_name = request.POST.get('app_name')
         host_list = request.POST.getlist('host_list')
         obj = models.Application.objects.create(name=app_name)
         obj.r.add(*host_list)
         return HttpResponse(json.dumps(ret))       
#-------------------------------------------------------------
from django.utils.safestring import mark_safe
#分页
#def user_list(request):
#        li = []
#        for i in range(100):
#            li.append(i)
#        return render(request,'user_list.html',{'li':li})  

#LIST = []
#for i in range(100):
#    LIST.append(i)
#def user_list(request):
#    current_page = request.GET.get('p')
#    current_page = int(current_page)
#    start = (current_page-1) * 10
#    end = current_page * 10 
#    data = LIST[start:end]
#    return render(request,'user_list.html',{'li':data}) 
#------
#------
LIST = []
for i in range(1050):
    LIST.append(i)
from utils import pagination
def user_list(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page,len(LIST))
    data = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/user_list/")
    


#    start = (current_page-1) * 10
#    end = current_page * 10
#    data = LIST[start:end]
#
#
#    all_count = len(LIST)
#    page_list = []
#    page_num =7
#    count,y = divmod(all_count,10)
#    if y:
#        count += 1
#    if count < page_num:
#       start_index = 1
#       end_index = count + 1
#    else:
#        if current_page <= (page_num+1)/2:
#            start_index = 1
#            end_index = page_num +1
#        else:
#            start_index = current_page - (page_num-1)/2
#            end_index = current_page + (page_num+1)/2
#            if ((page_num-1)/2) > count:
#                end_index = count + 1
#                start_index = count  - page_num + 1
#    if current_page == 1:
#        prev = '<a class="page" href="#">上一页</a>'
#    else:
#        prev = '<a class="page" href="/user_list/?p=%s">上一页</a>' % (current_page-1,)
#    page_list.append(prev)
#    for i in range(int(start_index),int(end_index)):
#        if i == current_page:
#            temp = '<a class="page active" href=/user_list/?p=%s>%s</a>' % (i,i)
#        else:
#        
#            temp = '<a class="page" href=/user_list/?p=%s>%s</a>' % (i,i)
#        page_list.append(temp)
#    if current_page == count:
#        nex = '<a class="page" href="#">下一页</a>'
#    else:
#        nex = '<a class="page" href="/user_list/?p=%s">下一页</a>' % (current_page+1,)
#    page_list.append(nex)
#    jump="""
#    <input type='text' /><a onclick='jumpTo(this,"/user_list/?p=");'>GO</a>
#    <script>
#        function jumpTo(ths,base){
#            var val = ths.previousSibling.value;
#            location.href = base + val;
#    } 
#    </script>
#    """
#    page_list.append(jump)
#    page_str = mark_safe("".join(page_list))
    return render(request,'user_list.html',{'li':data,'page_str':page_str})
#------
