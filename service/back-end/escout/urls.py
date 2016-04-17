from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'escout.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^collector/', include('escout.modules.collector.urls')),
                       url(r'^guard/', include('escout.modules.guard.urls')),
                       url(r'^dashboard/', include('escout.modules.dashboard.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
