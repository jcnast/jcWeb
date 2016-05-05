from django.db import models
from django.conf import settings

class Game(models.Model):
	title = models.CharField(max_length = 100)
	url = models.URLField(max_length = 200, null = True, blank = True)
	description = models.TextField()
	public = models.BooleanField(default = False)
	date = models.DateField(auto_now_add = True, auto_now = False)
	htmlFile = models.CharField(max_length = 200)
	headerPhoto = models.FileField(upload_to = settings.MEDIA_ROOT + '/games/headerPhotos', null = True, blank = True)
	iconPhoto = models.FileField(upload_to = settings.MEDIA_ROOT + '/games/iconPhotos', null = True, blank = True)
	downloadFile = models.FileField(upload_to = settings.MEDIA_ROOT + '/games/downloadFiles', null = True, blank = True)

	def __str__(self):
		return '%s' % (self.title)

	def get_downloadFile(self):
		if(self.downloadFile):
			return self.downloadFile
		elif(self.url):
			return self.url
		else:
			return False

class Series(models.Model):
	url = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	date = models.DateField(auto_now_add = True, auto_now = True)
	description = models.TextField()

	def __str__(self):
		return '%s' % (self.title)

class Analysis(models.Model):
	title = models.CharField(max_length = 100)
	series = models.ForeignKey('Series', null = True, blank = True)
	game = models.ForeignKey('Game', null = True, blank = True)
	url = models.URLField(max_length = 200, null = True, blank = True)
	public = models.BooleanField(default = False)
	date = models.DateField(auto_now_add = True, auto_now = False)
	description = models.TextField()
	htmlFile = models.CharField(max_length = 200)
	headerPhoto = models.FileField(upload_to = settings.MEDIA_ROOT + '/analysis/headerPhotos/', null = True, blank = True)

	def __str__(self):
		if(self.series):
			return '%s: %s' % (self.series.title, self.title)
		else:
			return '%s' % (self.title)

class Comment(models.Model):
	name = models.CharField(max_length = 100, null = True, blank = True)
	comment = models.TextField()
	analysis = models.ForeignKey('Analysis')
	date = models.DateField(auto_now_add = True)

	def __str__(self):
		return '%s: %s' % (self.analysis.title, self.name)
	