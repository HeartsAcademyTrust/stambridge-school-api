import django_filters 
from rest_framework.filters import BaseFilterBackend
from .models import Newsletter, Policy, Performance, StatutoryInfo, SchoolYear, Curriculum


class SchoolYearFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = SchoolYear
		depth = 2

class SchoolNewslettersFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = Newsletter
		depth = 1
		order_by = ['-date_published']

class SchoolPoliciesFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = Policy
		depth = 1

class SchoolStatutoryInfoFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = StatutoryInfo
		depth = 1
		order_by = ['-date_published']

class SchoolPerformanceFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = Performance
		depth = 1
		order_by = ['-date_published']

class SchoolCurriculumFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")

	class Meta:
		model = Curriculum
		depth = 1
		order_by = ['-date_published']