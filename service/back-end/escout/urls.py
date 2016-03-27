from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'escout.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^gazer/', include('escout.applications.gazer.urls')),
                       url(r'^dashboard/', include('escout.applications.dashboard.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
