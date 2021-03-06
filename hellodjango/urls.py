"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from testclass import views
#from login_home import views
urlpatterns = [
    url("",include("login_home.urls")),
    url("", include('user_info.urls')),
    url("", include('host.urls')),
    url("", include('host_test.urls')),
    url("", include('service_line.urls')),
    url(r'^admin/', admin.site.urls),
    ##url(r'^login/', views.login),
    #url(r'^home/', views.home),
    #url(r'^index/', views.index),
    #url(r'^test/', views.test.as_view()),
    ##url(r'^detail/', views.detail),
    #url(r'^detail-(\d+).html', views.detail),
    #url(r'^index2/', views.index2,name='xxxx'),
]
