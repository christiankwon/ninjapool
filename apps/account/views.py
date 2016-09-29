from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('carpool:index'))

    return render(request, 'account/index.html')


def register(request):
    if request.method == 'POST':
        response = User.objects.register(request.POST)

        if response[0]:
            messages.success(request, response[1])

        else:
            for msg in response[1]:
                messages.error(request, msg)


    return redirect(reverse('account:index'))


def login(request):
    if request.method == 'POST':
        response = User.objects.login(request.POST)

        if response[0]:
            request.session['user_id'] = response[2].id
            request.session['user_name'] = response[2].first_name + ' ' + response[2].last_name
            messages.success(request, response[1])
            return redirect(reverse('carpool:index'))

        else:
            messages.error(request, response[1])
            return redirect(reverse('account:index'))



def logout(request):
    if 'user_id' in request.session:
        request.session.clear()
        messages.success(request, "You have successfully logged out!")

    return redirect(reverse('account:index'))
