from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

DEPARTMENTS = (
	('Administration', 'Administration'),
	('Carson','Carson'),
	('Clinton','Clinton'),
	('Cumber','Cumberland'),
	("D's Place", "D's Place"),
	('Deer Lake', 'Deer Lake'),
	('Eastburn','Eastburn'),
	('Edmonds','Edmonds'),
	('Genesis','Genesis'),
	('Madison','Madison'),
	('Marine','Marine Drive'),
	('Oakland','Oakland'),
	('Sardis','Sardis'),
	('Victory','Victory'),
	('Willingdon','Willingdon'),
	('Options', 'Community Options'),
	('Action Packaging', 'Action Packaging'),
	('BEST', 'BEST'),
	('Outreach', 'Outreach'),
	('Childrens', 'Childrens')
	)

class Event(models.Model):
	user = models.ForeignKey(User, related_name="events")
	name = models.CharField(max_length=255)
	when = models.DateTimeField()
	where = models.CharField(max_length=255)
	instructor = models.CharField(max_length=255)
	description = models.TextField()
	capacity = models.PositiveIntegerField()
	public = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('training:detail', kwargs={'pk': self.id})

	def get_del_url(self):
		return reverse('training:event-delete', kwargs={'pk': self.id})

	def get_upd_url(self):
		return reverse('training:event-update', kwargs={'pk': self.id})


class Attendee(models.Model):
	event = models.ForeignKey(Event, related_name="attendees")
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=45)
	phone_number = models.CharField(max_length=20)
	department = models.CharField(max_length=20, choices=DEPARTMENTS)

	def __unicode__(self):
		return self.first_name

	def get_del_url(self):
		return reverse('training:attendee-delete', kwargs={'pk': self.id})
