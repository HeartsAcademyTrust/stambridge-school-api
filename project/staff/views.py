from rest_framework import filters
from rest_framework import generics
from .filters import SchoolDepartmentFilter
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListView(generics.ListAPIView):
	queryset = Department.objects.all().distinct()
	serializer_class = DepartmentSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolDepartmentFilter