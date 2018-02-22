from django.shortcuts import render
from pswdApp.form import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	return render(request,'display/index.html')

@login_required
def special_page(request):
	return HttpResponse("You are logged in now")


@login_required
def user_logout(request):
	return HttpResponse(reverse('index'))

def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)


		if user_form.is_valid() and profile_form.is_valid():

			subscriber = user_form.save()
			subscriber.set_password(subscriber.password)
			subscriber.save()


			profile = profile_form.save(commit=False)
			profile.subscriber = subscriber

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'display/register.html',
							{'user_form':user_form,
							'profile_form':profile_form,
							'registered':registered})


def user_login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('pswd')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('index')

			else:
				return HttpResponse("Account not active, you need to login")

		else:
			print("Someone tried to login and failed")
			print("Username: {} and Password: {}".format(username,password))
			return HttpResponse("Invalid login details entered, try again")
	else:
		return render(request,'display/login.html',{})
