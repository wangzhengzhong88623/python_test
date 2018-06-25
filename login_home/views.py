from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
class test(View):
     def get(self,request):
         print (request.method)
         return render(request,'test1.html')
     def post(self,request):
         print (request.method)

# Create your views here.
from django.shortcuts import HttpResponse
USER_LIST = [
     {'username':'wangzz','email':'363263458@qq.com','gender':'man'},
]

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == '123':
           return  redirect('/home/')
        else:
           error_msg = "用户名或密码错误"
    return render(request,'login.html' , {'error_msg': error_msg})
def home(request):
    if request.method == "POST":
      u = request.POST.get('username')
      e = request.POST.get('email')
      g = request.POST.get('gender')
      temp = {'username':u,'email':e,'gender':g}
      USER_LIST.append(temp)
    return render(request,'home.html',{'user_list':USER_LIST})


USER_DICT = {
     '1':{'name':'root1','email':'root@wangzz.com'},
     '2':{'name':'root2','email':'root@wangzz.com'},
     '3':{'name':'root3','email':'root@wangzz.com'},
     '4':{'name':'root4','email':'root@wangzz.com'},
     '5':{'name':'root5','email':'root@wangzz.com'},
}

def index(request):
    return render(request,'index.html',{'user_list':USER_DICT})
#def detail(request):
#    nid = request.GET.get('nid')
#    detail_info = USER_DICT[nid]
#    return render(request,'detail.html',{'detail_info':detail_info})
def detail(request,nid):
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})
def index2(request):
    print (request.path_info)
    from django.urls import reverse
    v = reverse('xxxx',args=(90,))
    print (v)
    return render(request,'index2.html',{'user_list':USER_DICT})
from login_home import models
def orm(request):
#     #models.userinfo.objects.create(username ='test',password ='123')
#     #obj = models.userinfo(username = 'wangzz',password = '123')
#     #obj.save()
#     #dic = {'username':'wangzz2','password':'123'}
#     #result = models.userinfo.objects.filter(username='test',id='2')
#     #for i in result:
#     #    print  (i.id,i.username,i.password)
#     #models.userinfo.objects.filter(id=4).delete()
#     #models.userinfo.objects.filter(id=3).update(password=66666)
     models.userinfo.objects.create(username ='wangzz',password ='password')
     return HttpResponse('ok')
#----------------
def login2(request):
     if request.method == "GET":
         return render(request,"login2.html")
     elif request.method == "POST":
         u = request.POST.get('user')
         p = request.POST.get('pwd')
         result = models.userinfo.objects.filter(username=u,password=p).first()
         if result:
                 print (result)
                 return  redirect('/home2/')
         else:
             return render(request,"error_login.html")
     else:
         return render(request,"方式非法")

def home2(request):
     return render(request,"home2.html")




