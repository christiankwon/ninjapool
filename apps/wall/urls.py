from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)', views.wall, name='wall'),
	url(r'^post_message/(?P<id>\d+)$', views.post_message, name="post_message"),
	url(r'^wall_message/(?P<id>\d+)$', views.wall_message, name="wall_message"),
	url(r'^users_list$', views.users_list, name="users_list"),
	url(r'^wall_create/(?P<id>\d+)', views.wall_create, name="wall_create"),
]
