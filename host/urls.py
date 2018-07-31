from django.conf.urls import url
from host import views
urlpatterns = [
    url(r'^host_management/', views.host_management),
]

