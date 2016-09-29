from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from . import models
from ..account.models import User

# Create your views here.
def index(request):
    return render(request, 'carpool/index.html')

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    stops = User.objects.filter(carpool_id=user.carpool_id)
    carpool = models.Carpool.objects.get(id=user.carpool_id)
    context = {'user':user, 'stops':stops, 'carpool':carpool}
    return render(request, 'carpool/index.html', context)


def checkin(request, checkinid):
    return redirect(reverse('carpool:index'))


def register(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to register as a driver.")
        return redirect(reverse('account:index'))

    if request.method == 'POST':
        response = models.Carpool.objects.new_carpool(request.POST, request.session['user_id'])


        if response[0]:
            messages.success(request, "Successfully registered as a driver.")
            return redirect(reverse('carpool:index'))
        else:
            messages.error(request, "Something went wrong with the registration.")
            return render(request, 'carpool/register.html')
