from django.shortcuts import render

# Create your views here.
from django.views import View
class test(View):
     def get(self,request):
         print (request.method)
         return render(request,'test1.html')
     def post(self,request):
         print (request.method)
