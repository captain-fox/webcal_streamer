from django.conf.urls import url
from web_client import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
]
