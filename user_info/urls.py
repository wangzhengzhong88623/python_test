from django.conf.urls import url
from user_info import views
urlpatterns = [
    url(r'^user_management/', views.user_management),
    url(r'^user_management-detail-(?P<nid>\d+)/', views.user_management_detail),
    url(r'^user_management-del-(?P<nid>\d+)/', views.user_management_del),
    url(r'^user_management-edit-(?P<nid>\d+)/', views.user_management_edit),
]

