import django_filters 
from rest_framework.filters import BaseFilterBackend
from .models import Newsletter, Policy


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