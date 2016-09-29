from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.wall, name='wall'),
	url(r'^post$', views.post_message, name="post_message"),
	url(r'^users_list$', views.users_list, name="users_list"),
]
