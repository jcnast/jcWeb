from django.db import models
from django.conf import settings

class Game(models.Model):
	title = models.CharField(max_length = 100)
	url = models.URLField(max_length = 200, null = True, blank = True)
	description = models.TextField()
	public = models.BooleanField(default = False)
	date = models.DateField(auto_now_add = True, auto_now = False)
	htmlFile = models.CharField(max_length = 200)
	headerPhoto = models.FileField(upload_to = 'games/headerPhotos', null = True, blank = True)
	iconPhoto = models.FileField(upload_to = 'games/iconPhotos', null = True, blank = True)
	downloadFile = models.FileField(upload_to = 'games/downloadFiles', null = True, blank = True)

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
	date = models.DateField(auto_now_add = True)
	description = models.TextField()

	def __str__(self):
		return '%s' % (self.title)

class Analysis(models.Model):
	title = models.CharField(max_length = 100)
	series = models.ForeignKey('Series', null = True, blank = True, on_delete = models.SET_NULL)
	game = models.ForeignKey('Game', null = True, blank = True, on_delete = models.SET_NULL)
	url = models.URLField(max_length = 200, null = True, blank = True)
	public = models.BooleanField(default = False)
	date = models.DateField(auto_now_add = True, auto_now = False)
	description = models.TextField()
	htmlFile = models.CharField(max_length = 200)
	headerPhoto = models.FileField(upload_to = 'analysis/headerPhotos/', null = True, blank = True)

	def __str__(self):
		if(self.series):
			return '%s: %s' % (self.series.title, self.title)
		else:
			return '%s' % (self.title)

class Comment(models.Model):
	name = models.CharField(max_length = 100, null = True, blank = True)
	comment = models.TextField()
	analysis = models.ForeignKey('Analysis', on_delete = models.CASCADE)
	date = models.DateField(auto_now_add = True)

	def __str__(self):
		return '%s: %s' % (self.analysis.title, self.name)
	
