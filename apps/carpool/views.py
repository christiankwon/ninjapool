from django.shortcuts import render, redirect
from ..account.models import User

# Create your views here.
def index(request):
    return render(request, 'carpool/index.html')
