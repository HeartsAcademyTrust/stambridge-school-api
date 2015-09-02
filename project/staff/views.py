from rest_framework import filters
from rest_framework import generics
from .filters import SchoolStaffFilter, SchoolVacancyFilter
from .models import Staff, Vacancy
from .serializers import StaffSerializer, VacancySerializer


class StaffListView(generics.ListAPIView):
	queryset = Staff.objects.all()
	serializer_class = StaffSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolStaffFilter

class VacancyListView(generics.ListAPIView):
	queryset = Vacancy.objects.all()
	serializer_class = VacancySerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolStaffFilter
