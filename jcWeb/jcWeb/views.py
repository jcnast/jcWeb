from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import simplejson
from requests import get
import os, re
from django.utils.datastructures import SortedDict

from subprocess import call

from jcWeb.models import *

#*********** home page ***********#
def home(request):
	# all games from newest to oldest
	games = Game.objects.all().order_by('-date')[:4]
	# analysis that are not a part of a series
	analysis = Analysis.objects.order_by('-date')[:4]

	context = {'download': False, 'games': games, 'analysis': analysis}
	return render(request, 'home.html', context)

#*********** bio pages ***********#
def bio(request):
	context = {'download': False}
	return render(request, 'bio.html', context)

def resume(request):
	context = {'download': True, 'downloadFile': '/media/resume/JaggerNast.pdf'}
	return render(request, 'resume.html', context)

#*********** game development pages ***********#
def games(request):
	# get all games to display
	games = Game.objects.all().order_by('-date')

	# pass along game objects
	context = {'download': False, 'games': games}
	return render(request, 'games.html', context)

def getgame(request, gameFile):
	# get game based on game file
	game = Game.objects.get(htmlFile = gameFile)
	download = True
	if(game.downloadFile):
		downloadFile = game.downloadFile
		downloadFile = str(downloadFile).split('jcWeb', 1)[1]
	elif(game.url):
		downloadFile = game.url
	else:
		downloadFile = False
	print downloadFile

	# pass along the game object
	context = {'download': download, 'downloadFile': downloadFile, 'game': game}
	return render(request, 'games/'+gameFile+'.html', context)

#*********** game design pages ***********#
def analysis(request):
	# all game analysis series
	series = Series.objects.all().order_by('-date')
	# dictionary with series as key and list of analysis as value
	seriesDict = SortedDict()
	for s in series:
		seriesDict[s] = Analysis.objects.filter(series__id = s.id).order_by('-date')[:2]
	# analysis that are not a part of a series
	analysis = Analysis.objects.filter(series__isnull = True)

	context = {'download': False, 'seriesDict': seriesDict, 'analysis': analysis}
	return render(request, 'analysis.html', context)

def series(request, series):
	# get requested series
	series = Series.objects.get(url = series)
	# get related analysis
	analysis = Analysis.objects.filter(series__id = series.id)

	context = {'series': series, 'analysis': analysis}
	return render(request, 'series/' + series.url + '.html', context)

def getanalysis(request, analysisFile):
	# get analysis based on analysis file
	analysis = Analysis.objects.get(htmlFile = analysisFile)
	# get comments on the analysis
	comments = Comment.objects.filter(analysis__id = analysis.id)

	# pass along the analysis file
	context = {'download': False, 'analysis': analysis, 'comments': comments}
	return render(request, 'analysis/' + analysisFile + '.html', context)

def comment(request, analysisFile):
	if(request.method == 'POST'):
		# commenter's name
		name = request.POST['name']
		# commenter's comment
		comment = request.POST['comment']
		# analysis commented on
		analysis = Analysis.objects.get(htmlFile = analysisFile)
		# as long as the comment is not empty create the comment
		if(comment != ''):
			newComment = Comment.objects.create(name=name, comment=comment, analysis=analysis)
	# send user back to analysis page
	return HttpResponseRedirect('/analysis/'+analysisFile)

def update(request):
	call("restart-server")
	return HttpResponseRedirect('/')
