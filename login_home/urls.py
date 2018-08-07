from django.conf.urls import url,include
from login_home import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^login2/', views.login2),
    url(r'^home/', views.home),
    url(r'^home2/', views.home2),
    url(r'^index/', views.index),
    url(r'^test/', views.test.as_view()),
    url(r'^detail/', views.detail),
    url(r'^detail-(\d+).html', views.detail),
    url(r'^index2/', views.index2,name='xxxx'),
    url(r'^orm/', views.orm),
    url(r'^login_cookie/',views.login_cookie),
    url(r'^login_cookie_index/',views.login_cookie_index),
]


