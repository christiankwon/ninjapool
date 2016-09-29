from django.shortcuts import render, redirect
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
    return render(request, 'carpool/register.html')