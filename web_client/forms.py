from django.forms import Form, ModelForm
from web_client.models import *


class ScheduleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ScheduleFile
        fields = ['file', 'title']
