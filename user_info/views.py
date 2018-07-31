from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse
from login_home import models

# Create your views here.
def user_management(request):
  if request.method == 'GET':
      user_list = models.UserInfo.objects.all()
      #其实user_list=(id,username,password,email,user_group_id(uid,caption))
      group_list = models.UserGroup.objects.all()
      return render(request,'user_management.html',{'user_list':user_list,'group_list':group_list})
  elif request.method == 'POST':
      u = request.POST.get('user')
      p = request.POST.get('pwd')
      e = request.POST.get('email')
      uid = request.POST.get('group_id')
      models.UserInfo.objects.create(username=u,password=p,email=e,user_group_id=uid)
      return redirect('user_management.html')
def user_management_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request,'user_management_detail.html',{'obj':obj})
def user_management_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    print (nid)
    return redirect('/user_management/')
def user_management_edit(request,nid):
    if request.method == "GET":
          obj = models.UserInfo.objects.filter(id=nid).first()
          return render(request,'user_management_edit.html',{'obj':obj})
    elif request.method == "POST":
          nid = request.POST.get('id')
          u   = request.POST.get('username')
          p   = request.POST.get('password')
          models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
          return redirect('/user_management/')
