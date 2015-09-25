from django.conf.urls import url
from .views import SchoolMenuView, SchoolYearView, SchoolNewslettersListView, SchoolPoliciesListView, SchoolStatutoryInfoListView


urlpatterns = [
    url(r'^(?P<school>[a-zA-z ]+)/school-menu/$', SchoolMenuView.as_view(), name='school-menu'),
    url(r'^years/$', SchoolYearView.as_view(), name='school-year'),
    url(r'^newsletters/$', SchoolNewslettersListView.as_view(), name='school-newsletters'),   
    url(r'^policies/$', SchoolPoliciesListView.as_view(), name='school-policies'),
    url(r'^statuatory-info/$', SchoolStatutoryInfoListView.as_view(), name='school-statutory-info'),
]