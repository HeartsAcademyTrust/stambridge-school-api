from rest_framework import filters, generics
from .filters import SchoolYearFilter, SchoolNewslettersFilter, SchoolPoliciesFilter, SchoolStatutoryInfoFilter
from .models import SchoolMenu, SchoolYear, Newsletter, Policy, StatutoryInfo
from .serializers import SchoolMenuSerializer, SchoolYearSerializer, SchoolNewslettersSerializer, SchoolPoliciesSerializer, SchoolStatutoryInfoSerializer

class SchoolYearView(generics.ListAPIView):
	queryset = SchoolYear.objects.all()
	serializer_class = SchoolYearSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolYearFilter

class SchoolMenuView(generics.RetrieveAPIView):
	queryset = SchoolMenu.objects.all()
	serializer_class = SchoolMenuSerializer
	lookup_field = 'school__name'
	lookup_url_kwarg = 'school'

class SchoolNewslettersListView(generics.ListAPIView):
	queryset = Newsletter.objects.all()
	serializer_class = SchoolNewslettersSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolNewslettersFilter

class SchoolPoliciesListView(generics.ListAPIView):
	queryset = Policy.objects.all()
	serializer_class = SchoolPoliciesSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolPoliciesFilter

class SchoolStatutoryInfoListView(generics.ListAPIView):
	queryset = StatutoryInfo.objects.all()
	serializer_class = SchoolStatutoryInfoSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolStatutoryInfoFilter