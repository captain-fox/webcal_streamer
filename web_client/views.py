from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from web_client.forms import *
from web_client.converter.FileHandler import *
from web_client.converter.Event import *


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


class Converter(TemplateView):
    template_name = 'homepage/preview.html'

    def get_context_data(self, **kwargs):

        file = ScheduleFile.objects.first()
        working_copy = FileHandler.read_csv_file(file.file.path, InputConverter.__HEADERS__)
        Event.import_csv_to_db(working_copy)
        events = RawCSVEvent.objects.all()

        context = super(Converter, self).get_context_data(**kwargs)
        context['file'] = file
        context['events'] = events

        return context
