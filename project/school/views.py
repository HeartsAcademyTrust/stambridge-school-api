from rest_framework import filters, generics
from .filters import SchoolNewslettersFilter, SchoolPoliciesFilter, SchoolStatuatoryInfoFilter
from .models import SchoolMenu, Newsletter, Policy, StatuatoryInfo
from .serializers import SchoolMenuSerializer, SchoolNewslettersSerializer, SchoolPoliciesSerializer, SchoolStatuatoryInfoSerializer


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

class SchoolStatuatoryInfoListView(generics.ListAPIView):
	queryset = StatuatoryInfo.objects.all()
	serializer_class = SchoolStatuatoryInfoSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = SchoolStatuatoryInfoFilter