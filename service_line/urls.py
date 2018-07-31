from django.conf.urls import url
from service_line import views
urlpatterns = [
    url(r'^service_line_management/',views.service_line_management),
]

