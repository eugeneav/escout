from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', 'escout.views.home', name='home'),
    url(r'^collector/', include('escout.collector.urls')),
    url(r'^guard/', include('escout.guard.urls')),
    url(r'^dashboard/', include('escout.dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
