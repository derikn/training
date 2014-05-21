from django.contrib import admin
from training.models import Attendee, Event

class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [AttendeeInline]

admin.site.register(Event, EventAdmin)