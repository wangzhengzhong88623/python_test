from django.conf.urls import url
from host_test import views
urlpatterns = [
    url(r'^business/$', views.business),
    url(r'^host/$', views.host),
]

