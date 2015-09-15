from django.conf.urls import url
from .views import SchoolMenuView, SchoolNewslettersListView, SchoolPoliciesListView, SchoolStatuatoryInfoListView


urlpatterns = [
    url(r'^(?P<school>[a-zA-z ]+)/school-menu/$', SchoolMenuView.as_view(), name='school-menu'),
    url(r'^newsletters/$', SchoolNewslettersListView.as_view(), name='school-newsletters'),   
    url(r'^policies/$', SchoolPoliciesListView.as_view(), name='school-policies'),
    url(r'^statuatory-info/$', SchoolStatuatoryInfoListView.as_view(), name='school-statuatory-info'),
]