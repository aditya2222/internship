from django.db import models

# Create your models here.


class mainContent(models.Model):
	name = models.CharField(max_length=126)
	question = models.TextField()
	Answer = models.TextField()

	def __str__(self):
		return self.name

