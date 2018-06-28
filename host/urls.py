from django.conf.urls import url
from host import views
urlpatterns = [
    url(r'^ssets_see/', views.host_see),
    url(r'^assets_management/', views.host_management),
]

