from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Wall, Message
from ..account.models import User


def wall(request, id):
    if 'user_id' not in request.session:
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


def wall_message(request, id):
    if request.method == 'POST':
        response = Message.objects.new_message(request.POST['message_body'], request.session['user_id'], id)

        if response[0]:
            messages.success(request, response[1])
        else:
            for msg in response[1]:
                messages.error(request, msg)
            return redirect(reverse('carpool:dashboard'))

    return redirect(reverse('carpool:dashboard'))


def post_message(request, id):
    if request.method == 'POST':
        response = Message.objects.new_message(request.POST['message_body'], request.session['user_id'], id)

        if not response[0]:
            for msg in response[1]:
                messages.error(request, msg)

            return redirect(reverse('wall:wall', kwargs={'id':id}))

    return redirect(reverse('wall:wall', kwargs={'id':id}))


def wall_create(request, id):
    wall = Wall.objects.create_wall(id, request.session['user_id'])

    return redirect(reverse('wall:wall', kwargs={'id':wall.id}))
