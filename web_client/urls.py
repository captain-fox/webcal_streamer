from django.conf.urls import url
from web_client import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^upload/$', views.FileUpload.as_view(), name='upload'),
    url(r'^import-schedule/$', views.Converter.as_view(), name='import_events'),
    url(r'^ajax/schedule-files/$', views.ScheduleFiles.as_view(), name='load_schedule_files'),
    # url(r'^search/$', views.Search.as_view(), name='search'),
]
