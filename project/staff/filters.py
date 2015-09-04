import django_filters 
from rest_framework.filters import BaseFilterBackend
from .models import Staff, Vacancy


class SchoolStaffFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")
	department = django_filters.CharFilter(name="department__name")

	class Meta:
		model = Staff
		depth = 1

class SchoolVacancyFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")
	department = django_filters.CharFilter(name="department__name")

	class Meta:
		model = Vacancy
		depth = 1