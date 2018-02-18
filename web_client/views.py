from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from web_client.forms import *
from web_client.converter.FileHandler import *
from web_client.converter.Event import *
import csv


class HomePage(TemplateView):
    template_name = 'homepage/index.html'


class FileUpload(View):
    template_name = 'upload/upload.html'

    def get(self, request):
        form = ScheduleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ScheduleForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('homepage')

        return render(request, self.template_name, {'form': form})


class Converter(View):
    template_name = 'homepage/test.html'

    def get(self, request):
        file = ScheduleFile.objects.first()
        working_copy = FileHandler.read_csv_file(file.file.path, InputConverter.__HEADERS__)
        Event.collect_events_for_group(working_copy)

        events = RawCSVEvent.objects.all()
        count = events.count()

        return render(request, self.template_name, {'file': file, 'events': events, 'count': count})

    def post(self, request):
        pass
