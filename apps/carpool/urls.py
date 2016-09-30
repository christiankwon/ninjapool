from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^add_car$', views.add_car, name='add_car'),
    url(r'^join/(?P<carpool_id>[0-9]+)$', views.join, name='join'),
    url(r'^new_carpool$', views.new_carpool, name='new_carpool'),
    url(r'^new_carpool_create$', views.new_carpool_create, name='new_carpool_create'),
    url(r'^nearby$', views.nearby, name='nearby'),
    url(r'^leave$', views.leave, name='leave'),
    url(r'^view_carpool/(?P<carpool_id>[0-9]+)$', views.view_carpool, name='view_carpool'),
]
