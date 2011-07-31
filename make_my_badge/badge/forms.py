from django.forms import ModelForm
from badge.models import Event

class EventSubmissionForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('user','zipped_content')
