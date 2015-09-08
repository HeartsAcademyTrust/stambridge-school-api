import django_filters 
from rest_framework.filters import BaseFilterBackend
from .models import Event

class EventFilter(django_filters.FilterSet):
	school = django_filters.CharFilter(name="school__name")
	min_date = django_filters.DateTimeFilter(name='start_time', lookup_type='gte')
	max_date = django_filters.DateTimeFilter(name='start_time', lookup_type='lte')

	class Meta:
		model = Event
		depth = 1
		order_by = ['start_time']