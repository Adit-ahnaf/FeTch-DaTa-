from django.db import models

# Create your models here.
class Data(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	profession = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.name} '
