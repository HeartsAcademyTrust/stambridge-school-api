from django.conf.urls import url
from .views import StaffListView, VacancyListView


urlpatterns = [
    url(r'^staff/$', StaffListView.as_view(), name='staff'),
    url(r'^vacancies/$', VacancyListView.as_view(), name='vacancies'),
]