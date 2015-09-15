	# SCHOOL_CHOICES = (
	# 	(BRISCOE, 'Brisoe Primary School and Nursery'),
	# 	(WICKFORD, 'Wickford Church of England School'),
	# 	(WATERMAN, 'Waterman Primary School'),
	# 	(STAMBRIDGE, 'Stambridge Primary School'),
	# 	(HEARTS, 'Hearts Academy Trust')
	# )
from django.db import models
from django.utils import timezone


class School(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class SchoolYear(models.Model):
	school = models.ForeignKey(School)
	year = models.CharField(max_length=20)

	def  __str__(self):
		return self.school.name + ': ' + self.year

class SchoolMenu(models.Model):
	school = models.OneToOneField(School)
	menu = models.FileField(upload_to='documents')

	def __str__(self):
		return self.school.name + ' menu'

class Newsletter(models.Model):
	school = models.ForeignKey(School)
	date_published = models.DateField(default=timezone.now)
	file = models.FileField(upload_to='newsletters')

	def __str__(self):
		return self.school.name + ': ' + str(self.date_published)

class Policy(models.Model):
	school = models.ForeignKey(School)
	title = models.CharField(max_length=50)
	date_published = models.DateField(default=timezone.now)
	file = models.FileField(upload_to='policies')

	def __str__(self):
		return self.school.name + ': ' + self.title

class StatuatoryInfo(models.Model):
	school = models.ForeignKey(School)
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	date_published = models.DateField(default=timezone.now)
	file = models.FileField(upload_to='statuaryInfo', null=True)

	def __str__(self):
		return self.school.name + ': ' + self.title + ' - ' + str(self.date_published)
