from django.shortcuts import render, redirect
from ..account.models import User
# Create your views here.
def wall(request):
	return render(request, 'wall/test.html')

def post_message(request):
	if request.method == 'POST':
		response = Wall.objects.new_message(request.POST)
	return redirect('wall:wall')

def users_list(request):
	users = User.objects.exclude(id=request.session['user_id'])
	context = {
		"users": users
	}
	return render(request, 'wall/userMessageTest.html', context)
