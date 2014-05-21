from __future__ import absolute_import

from django.db.models import Count
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from braces import views
from . import models
from . import forms

class RestrictToUserMixin(object):
	def get_queryset(self):
		queryset = super(RestrictToUserMixin, self).get_queryset()
		queryset = queryset.filter(user = self.request.user)
		return queryset

class EventDetailView(
	views.LoginRequiredMixin,
    views.PrefetchRelatedMixin,
    generic.DetailView
):
    form_class = forms.AttendeeForm
    http_method_names = ['get', 'post']
    model = models.Event
    prefetch_related = ('attendees',)

    def get(self, request, *args, **kwargs):
    	self.object = self.get_object()
    	if not self.object.public:
    		return HttpResponseRedirect(reverse('training:list'))
    	else:
    		context = self.get_context_data(object=self.object)
    		return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context.update({'form': self.form_class(self.request.POST or None)})
        event = self.object
        context['attendee_count'] = event.attendees.count()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            attendee = form.save(commit=False)
            attendee.event = obj
            attendee.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj)


class EventListView(
	views.LoginRequiredMixin,
	generic.ListView):
    model = models.Event

    def get_queryset(self):
        queryset = models.Event.objects.all().filter(public = True).order_by('when')
       #queryset = queryset.annotate(attendee_count=Count('attendees'))
        return queryset

class EventScheduleView(
	generic.ListView):
	model = models.Event
	template_name = 'training/schedule.html'

	def get_queryset(self):
		queryset = models.Event.objects.all().filter(public =True).order_by('when')
		return queryset

class EventCreateView(
	views.LoginRequiredMixin,
	views.SetHeadlineMixin,
	views.PermissionRequiredMixin,
	generic.CreateView):

	form_class = forms.EventForm
	headline = 'Create'
	model = models.Event
	permission_required = "training.add_event"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(EventCreateView, self).form_valid(form)


