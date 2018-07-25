from django.conf.urls import url
from host import views
urlpatterns = [
    url(r'^service_line_management/',views.service_line_management),
    url(r'^host_management/', views.host_management),
]

