from django.contrib import admin
from jcWeb.models import *

class GameAdmin(admin.ModelAdmin):
	fields = ['title', 'url', 'description', 'public', 'date', 'htmlFile', 'headerPhoto', 'iconPhoto', 'downloadFile']

class SeriesAdmin(admin.ModelAdmin):
	fields = ['url', 'title', 'date', 'description']

class AnalysisAdmin(admin.ModelAdmin):
	fields = ['title', 'series', 'game', 'url', 'public', 'date', 'description', 'htmlFile', 'headerPhoto']

class CommentAdmin(admin.ModelAdmin):
	fields = ['name', 'comment', 'analysis', 'date']

admin.site.register(Game)
admin.site.register(Series)
admin.site.register(Analysis)
admin.site.register(Comment)
