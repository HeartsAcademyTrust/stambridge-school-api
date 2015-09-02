from django.db import models
from school.models import School


class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Staff(models.Model):
	name = models.CharField(max_length=50)
	school = models.ForeignKey(School)
	role = models.CharField(max_length=50)
	department = models.ForeignKey(Department)
	photo = models.ImageField(upload_to='images')

	def __str__(self):
		return self.name

class Vacancy(models.Model):
	school = models.ForeignKey(School)
	role = models.CharField(max_length=50)
	department = models.ForeignKey(Department)
	description = models.TextField()

	def __str__(self):
		return self.department + ': ' + self.role