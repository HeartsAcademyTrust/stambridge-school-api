import django_filters 
from rest_framework.filters import BaseFilterBackend
from .models import Department


class SchoolDepartmentFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = Department
		depth = 2