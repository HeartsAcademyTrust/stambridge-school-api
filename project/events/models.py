from django.db import models
from school.models import School
from django.utils import timezone


class Event(models.Model):
	school = models.ForeignKey(School)
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	start_time = models.DateTimeField(default=timezone.now)
	end_time = models.DateTimeField(null=True)
	holiday = models.BooleanField(default=False)

	def __str__(self):
		return self.school.name + ': ' + self.name
