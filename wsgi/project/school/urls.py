from django.conf.urls import url
from .views import SchoolAdmissionsView, SchoolMenuView, SchoolCurriculumView, SchoolYearView, SchoolNewslettersListView, SchoolPoliciesListView, SchoolStatutoryInfoListView, SchoolPerformanceListView


urlpatterns = [
    url(r'^(?P<school>[a-zA-z ]+)/school-menu/$', SchoolMenuView.as_view(), name='school-menu'),
    url(r'^(?P<school>[a-zA-z ]+)/school-curriculum/$', SchoolCurriculumView.as_view(), name='school-curriculum'),
    url(r'^(?P<school>[a-zA-z ]+)/school-admissions/$', SchoolAdmissionsView.as_view(), name='school-admissions'),
    url(r'^years/$', SchoolYearView.as_view(), name='school-year'),
    url(r'^newsletters/$', SchoolNewslettersListView.as_view(), name='school-newsletters'),   
    url(r'^policies/$', SchoolPoliciesListView.as_view(), name='school-policies'),
    url(r'^statuatory-info/$', SchoolStatutoryInfoListView.as_view(), name='school-statutory-info'),
    url(r'^performance/$', SchoolPerformanceListView.as_view(), name='school-performance'),
]