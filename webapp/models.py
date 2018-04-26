from django.db import models

# Create your models here.


class mainContent(models.Model):
	name = models.CharField(max_length=126)
	question = models.TextField()
	Answer = models.TextField()

	def __str__(self):
		return self.name



class Topic(models.Model):
	title = models.CharField(max_length=126,null=True)
	question = models.TextField(null=True)
	answer = models.TextField(null=True)

	def __str__(self):
		return self.title



class Subject(models.Model):
	title = models.CharField(max_length=126,default='title')
	TopictLinked = models.ManyToManyField(Topic)

	def __str__(self):
		return self.title



class Grade(models.Model):
	GradeName = models.CharField(max_length=126)
	SubjectLinked = models.ManyToManyField(Subject)
	def __str__(self):
		return self.GradeName

