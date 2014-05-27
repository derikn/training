from __future__ import absolute_import
import datetime
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from datetimewidget.widgets import DateTimeWidget


from . import models	

class EventForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'when','where','instructor','description', 'capacity')
        model = models.Event
        widgets = {
            #Use localization
            'when': DateTimeWidget(attrs={'class':"datetimeinput"}, usel10n = True)
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'when',
            'where',
            'instructor',
            'capacity',
            'description',
            ButtonHolder(
                Submit('create', 'Create', css_class='btn-primary')
            )
        )

    def clean_when(self):
        when = self.cleaned_data.get('when')
        if when < timezone.now():
            raise ValidationError("Cannot create Event in the past")
        return when

class EventUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'when','where','instructor','description', 'capacity')
        model = models.Event
        widgets = {
            #Use localization
            'when': DateTimeWidget(attrs={'class':"datetimeinput"}, usel10n = True)
        }

    def __init__(self, *args, **kwargs):
        super(EventUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'when',
            'where',
            'instructor',
            'capacity',
            'description',
            ButtonHolder(
                Submit('update', 'Update', css_class='btn-primary')
            )
        )
class AttendeeForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'department')
        model = models.Attendee

    def __init__(self, *args, **kwargs):
        super(AttendeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'department',
            ButtonHolder(
                Submit('add', 'Add', css_class='btn-primary')
            )
        )