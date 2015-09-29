from django.conf.urls import url
from .views import EventListView


urlpatterns = [
    url(r'^$', EventListView.as_view(), name='school-events'),
]