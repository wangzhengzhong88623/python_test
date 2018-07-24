from django.conf.urls import url
from host_test import views
urlpatterns = [
    url(r'^business/$', views.business),
    url(r'^host/$', views.host),
    url(r'^test_ajax/$', views.test_ajax),
    url(r'^test_app/$', views.test_app),
    url(r'^ajax_add_app/$', views.ajax_add_app),
]

