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

class SchoolMenu(models.Model):
	school = models.OneToOneField(School)
	menu = models.FileField(upload_to='documents')

	def __str__(self):
		return self.school.name + ' menu'

class Newsletter(models.Model):
	school = models.ForeignKey(School)
	date_published = models.DateField(default=timezone.now)
	file = models.FileField(upload_to='documents')

	def __str__(self):
		return self.school.name + ': ' + str(self.date_published)

class Policy(models.Model):
	school = models.ForeignKey(School)
	title = models.CharField(max_length=50)
	date_published = models.DateField(default=timezone.now)
	file = models.FileField(upload_to='documents')

	def __str__(self):
		return self.school.name + ': ' + self.title
