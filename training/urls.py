from __future__ import absolute_import

from django.conf.urls import patterns, url, include
from training import views

urlpatterns = patterns ('',
	url(r'^$', views.EventListView.as_view(), name='list'),
	url(r'^hidden/(?P<slug>[-\w]+)/$', views.EventDetailView.as_view(), name='slug'),
	url(r'^d/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='detail'),
	url(r'^create/$', views.EventCreateView.as_view(), name='create'),
	url(r'^s/', views.EventScheduleView.as_view(), name='schedule'),

	#url(r'^s/(?P<slug>[-\w]+)/$', views.EventScheduleView.as_view(), name='schedule'),
	)