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
     username = 'root'
     password = 'password'
     email =  '363263458@qq.com'
     models.UserGroup.objects.create(uid ='1',caption='admin')
     models.UserInfo.objects.create(username = username ,password =password,email= email,user_group_id='1')
     return HttpResponse('管理员:%s,密码:%s,邮箱:%s' % (username,password,email))
#----------------
def login2(request):
     if request.method == "GET":
         return render(request,"login2.html")
     elif request.method == "POST":
         u = request.POST.get('user')
         p = request.POST.get('pwd')
         result = models.UserInfo.objects.filter(username=u,password=p).first()
         if result:
                 print (result)
                 return  redirect('/home2/')
         else:
             return render(request,"error_login.html")
     else:
         return render(request,"方式非法")

def home2(request):
     return render(request,"home2.html")


######cookie######
user_info = {
    'wangzhengzhong':{'pwd':"password"},
    'fengkun':{'pwd':"password"},
}
def login_cookie(request):
    if request.method == "GET":
        return render(request,'login_cookie.html')
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("pwd")
        dic = user_info.get(u)
        if not dic:
            return render(request,'login_cookie.html')
        if dic['pwd'] == p:
            res = redirect('/login_cookie_index/')
            #res.set_cookie('username111',u,max_age=10)
            import datetime
            current_date = datetime.datetime.utcnow()
            current_date = current_date + datetime.timedelta(seconds=5)
            res.set_cookie('username111',u,expires=current_date)
            return res
        else:
            return render(request,'login_cookie.html')
def login_cookie_index(request):
    v = request.COOKIES.get('username111')
    if not v:
       return redirect("/login_cookie/")
    return render(request,'login_cookie_index.html',{'current_user':v})
def cookie(request):
    request.COOKIES
    request.COOKIES['username111']
    request.COOKIES.get('username111')
    response = render(request,'login_cookie_index.html')
    response = redirect('/login_cookie_index/')
    # 设置cookie,关闭浏览器失效
    response.set_cookie('key',"value")
    # 设置cookie,N秒只有失效
    response.set_cookie('username111',"value",max_age=10)
    # 设置cookie,截止时间失效
    import datetime
    current_date = datetime.datetime.utcnow()
    current_date = current_date + datetime.timedelta(seconds=5)
    res.set_cookie('username111',u,expires=current_date)
###############session+cookie#####################
def login_session(request):
    if request.method == "GET":
        return render(request,'login_session.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            #生成随机字符串
            #写道用户浏览器cookie
            #保存到session中
            #在随机字符串对应的字典中设置相关内容
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb',None) == '1': #认为设置超时时间(默认两周)
                request.session.set_expiry(10) #session过期时间10秒
            return redirect('/index_session/')
        else:
            return render(request,'login_session.html')
def index_session(request):
    #获取当前用户随机字符
    #根据随机字符获取对应信息
    if request.session.get('is_login',None):
        return render(request,'index_session.html',{'username':request.session['username']})
    else:
        return HttpResponse('GUN!')
def logout_session(request):
    request.session.clear()
    return redirect('/login_session/')
