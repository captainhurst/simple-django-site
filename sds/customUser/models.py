from django.db import models

# Create your models here.


class emailCaptureModel(models.Model):
	email = models.EmailField(max_length=100,blank=True, null= True, unique= True)
	firstName = models.CharField(max_length=20, null=True, blank=True)
	lastName = models.CharField(max_length=20, null=True, blank=True)
	zipCode = models.IntegerField(null=True, blank=True)
	dateAdded = models.DateField(auto_now_add=True)
		
	def __unicode__(self):
		return self.email

	class Meta:
	   ordering = ['lastName', 'firstName']

