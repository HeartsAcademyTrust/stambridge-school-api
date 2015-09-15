from django.conf.urls import url
from .views import DepartmentListView


urlpatterns = [
		url(r'^departments/$', DepartmentListView.as_view(), name='department')
]