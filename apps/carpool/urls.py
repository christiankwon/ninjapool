from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkin/(?P<checkinid>[0-9]+$)', views.checkin, name='checkin'),
    url(r'^register$', views.register, name='register'),
]
