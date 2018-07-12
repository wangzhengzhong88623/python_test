from django.conf.urls import url
from host_test import views
urlpatterns = [
    url(r'^ssets_test_see/', views.host_test_see),
]

