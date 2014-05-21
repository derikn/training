from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

DEPARTMENTS = (
	('Admin', 'Administration'),
	('Carson','Carson'),
	('Clinton','Clinton'),
	('Cumber','Cumberland'),
	('Ds',"D's Place"),
	('Deer', 'Deer Lake'),
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
	('AP', 'Action Packaging'),
	('BEST', 'BEST'),
	('Outreach', 'Outreach'),
	('Childrens', 'Childrens')
	)

class Event(models.Model):
	user = models.ForeignKey(User, related_name="events")
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank = True)
	when = models.DateTimeField()
	where = models.CharField(max_length=255)
	host = models.CharField(max_length=255)
	capacity = models.IntegerField()
	public = models.BooleanField()

	def __unicode__(self):
		return self.name

	def get_slug_url(self):
		return reverse('training:slug', kwargs={'slug': self.slug})
	def get_absolute_url(self):
		return reverse('training:detail', kwargs={'pk': self.id})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Event, self).save(*args, **kwargs)

class Attendee(models.Model):
	event = models.ForeignKey(Event, related_name="attendees")
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=254)
	phone_number = models.CharField(max_length=20)
	department = models.CharField(max_length=10, choices=DEPARTMENTS)

	def __unicode__(self):
		return self.first_name