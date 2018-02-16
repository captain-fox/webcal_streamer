from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from web_client.forms import *


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
