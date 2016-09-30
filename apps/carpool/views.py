from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

import json
from django.core.serializers.json import DjangoJSONEncoder

from . import models
from ..account.models import User, Car

# Create your views here.
def index(request):
    return render(request, 'carpool/index.html')


def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in.")
        return redirect(reverse('account:index'))

    user = User.objects.get(id=request.session['user_id'])
    stops = User.objects.filter(carpool_id=user.carpool_id)
    carpool = models.Carpool.objects.filter(id=user.carpool_id)
    cars = Car.objects.filter(owner=user)

    context = {'user':user, 'stops':stops, 'carpool':carpool, 'cars':cars}

    return render(request, 'carpool/index.html', context)


def checkin(request, checkinid):
    return redirect(reverse('carpool:dashboard'))

def nearby(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in.")
        return redirect(reverse('account:index'))

    all_users = User.objects.exclude(id=request.session['user_id']).values_list('id', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'arrive_by')
    json_users = json.dumps(list(all_users), cls=DjangoJSONEncoder)

    context = {
        'me': User.objects.get(id=request.session['user_id']),
        'all_users': all_users,
        'json_users': json_users,
        'dojo_address': "10777 Main St #100, Bellevue, WA 98004",
    }
    return render(request, 'carpool/nearby.html', context)


def add_car(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to add a car.")
        return redirect(reverse('account:index'))

    if request.method == 'POST':
        response = User.objects.new_car(request.POST, request.session['user_id'])

        if response[0]:
            messages.success(request, response[1])
            return redirect(reverse('carpool:dashboard'))

        else:
            messages.error(request, response[1])
            return render(request, 'carpool/add_car.html')

    return render(request, 'carpool/add_car.html')


def join(request):
    return redirect(reverse('carpool:nearby'))


def create(request):
    return redirect(reverse('carpool:dashboard'))
