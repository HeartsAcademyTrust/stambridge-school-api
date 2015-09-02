from django.conf.urls import url
from .views import SchoolMenuView, SchoolNewslettersListView, SchoolPoliciesListView


urlpatterns = [
    url(r'^(?P<school>[a-zA-z ]+)/schoolmenu/$', SchoolMenuView.as_view(), name='school-menu'),
    url(r'^newsletters/$', SchoolNewslettersListView.as_view(), name='school-newsletters'),
    url(r'^policies/$', SchoolPoliciesListView.as_view(), name='school-policies'),
]