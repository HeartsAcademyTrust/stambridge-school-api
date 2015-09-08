from django.shortcuts import render
from rest_framework import filters, generics
from .filters import EventFilter
from .models import Event
from .serializers import EventSerializer

class EventListView(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = EventFilter
