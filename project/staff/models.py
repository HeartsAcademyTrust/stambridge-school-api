from django.db import models
from school.models import School


class Department(models.Model):
	name = models.CharField(max_length=50)
	school = models.ForeignKey(School)

	def __str__(self):
		return self.school.name + ': ' + self.name

class Staff(models.Model):
	name = models.CharField(max_length=50)
	role = models.CharField(max_length=50, blank=True)
	department = models.ForeignKey(Department, related_name='staff')
	extra_info = models.TextField(blank=True)
	photo = models.ImageField(upload_to='images')

	class Meta:
		unique_together = ('department', 'id')
		ordering = ['name']

	def __str__(self):
		return self.department.school.name + ': ' + self.name

class Vacancy(models.Model):
	role = models.CharField(max_length=50)
	department = models.ForeignKey(Department, related_name='vacancies')
	description = models.TextField(blank=True)

	class Meta:
		unique_together = ('department', 'id')
		ordering = ['role']

	def __str__(self):
		return self.department.school.name + ' ' + self.department.name + ': ' + self.role