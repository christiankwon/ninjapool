from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Wall, Message
from ..account.models import User
# Create your views here.


def wall(request, id):
	if not 'user_id' in request.session:
		return redirect('wall:users_list')

	user = User.objects.get(id=request.session['user_id'])
	if not Wall.objects.filter(users__id=user.id).filter(id=id):
		return redirect('wall:users_list')

	wall = Wall.objects.get(id=id)
	posts = Message.objects.filter(walls=wall)
	context = {
		'wall': wall,
		'posts': posts,
	}
	return render(request, 'wall/wall.html', context)


def post_message(request, id):

	if request.method == 'POST':
		response = Message.objects.new_message(request.POST['message_body'], request.session['user_id'], id)

		if response[0]:
			messages.success(request, response[1])
		else:
			for msg in response[1]:
				messages.error(request, msg)
			return redirect(reverse('wall:wall', kwargs={'id':id}))

	return redirect(reverse('wall:wall', kwargs={'id':id}))


def users_list(request):
	walls = Wall.objects.all()
	users = User.objects.exclude(id=request.session['user_id'])
	context = {
		"users": users,
		"walls":walls,
	}
	return render(request, 'wall/userMessageTest.html', context)

def wall_create(request, id):
	wall = Wall.objects.create_wall(id, request.session['user_id'])

	return redirect(reverse('wall:wall', kwargs={'id':wall.id}))
