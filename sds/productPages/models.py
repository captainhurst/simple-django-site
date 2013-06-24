from django.db import models

# Create your models here.


class PageModel(models.Model):
	isLive = models.BooleanField(default=True)
	titleTag = models.CharField(max_length=255, null=True, blank=True, default=None)
	metaDescription = models.CharField(max_length=255, null=True, blank=True, default=None)
	descriptiveUrl = models.CharField(max_length=255)
	categories = models.ManyToManyField('Categories')
	pageContent = models.TextField(null=True, blank=True, default=None)
	anchorText = models.CharField(max_length=140)
	articleHeader = models.CharField(max_length=255)
		
	def __unicode__(self):
		return self.articleHeader

	class Meta:
	   ordering = ['articleHeader']


class Categories(models.Model):
	categoryName = models.CharField(max_length=255, default=None)
	
	def __unicode__(self):
		return self.categoryName

	class Meta:
		ordering = ['categoryName']


class PageViewCount(models.Model):
	page = models.ForeignKey(PageModel)
	numberOfViews = models.IntegerField()
	
	def __unicode__(self):
		return self.page

	class Meta:
		ordering = ['-numberOfViews']


class HomePageModels(models.Model):
	titleTag = models.CharField(max_length=255, null=True, blank=True, default=None)
	metaDescription = models.CharField(max_length=255, null=True, blank=True, default=None)
	pageContent = models.TextField(null=True, blank=True, default=None)
	articleHeader = models.CharField(max_length=255)

	def __unicode__(self):
		return self.articleHeader

	class Meta:
	   ordering = ['articleHeader']