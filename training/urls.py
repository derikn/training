from __future__ import absolute_import

from django.conf.urls import patterns, url, include
from training import views

urlpatterns = patterns ('',
	#EventURLs
	url(r'^$', views.EventListView.as_view(), name='list'),
	url(r'^d/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='detail'),
	url(r'^create/$', views.EventCreateView.as_view(), name='create'),
	url(r'^e/(?P<pk>\d+)/$', views.EventUpdateView.as_view(), name='event-update'),
	url(r'^s/', views.EventScheduleView.as_view(), name='schedule'),
	url(r'^del/(?P<pk>\d+)/$', views.EventDeleteView.as_view(),
        name='event-delete'),
	#AttendeeURLs
	url(r'^attendee/del/(?P<pk>\d+)/$', views.AttendeeDeleteView.as_view(),
        name='attendee-delete'),

	#url(r'^s/(?P<slug>[-\w]+)/$', views.EventScheduleView.as_view(), name='schedule'),
	)