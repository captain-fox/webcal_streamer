from django.conf.urls import url
from web_client import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^upload/$', views.FileUpload.as_view(), name='upload'),
]
