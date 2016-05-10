from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from jcWeb import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
# home page
    url(r'^$', views.home),
# bio pages
    url(r'^bio/$', views.bio),
    url(r'^resume/$', views.resume),
# game develpoment pages
    url(r'^games/$', views.games),
    url(r'^games/(?P<gameFile>.*)/$', views.getgame),
# game design pages
    url(r'^analysis/$', views.analysis),
    url(r'^analysis/series/(?P<series>.*)/$', views.series),
    url(r'^analysis/comment/(?P<analysisFile>.*)/$', views.comment),
    url(r'^analysis/(?P<analysisFile>.*)/$', views.getanalysis),
# update the website
    # url(r'^update/$', views.update),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
