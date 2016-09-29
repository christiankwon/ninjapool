from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^checkin/(?P<checkinid>[0-9]+$)', views.checkin, name='checkin'),
    url(r'^add_car$', views.add_car, name='add_car'),
    url(r'^join$', views.join, name='join'),
    url(r'^create$', views.create, name='create'),
]
