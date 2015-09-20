from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from login.models import Role
from login.models import UserProfile
from login.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


## index view
def index(request):
	if request.user.is_authenticated():
		return redirect('/home')
	context_dict = {}
	return render(request, 'login/index.html', context_dict)
### for login
def login(request):
	if request.user.is_authenticated():
		return redirect('/home')
	if request.method == 'POST':
		username = request.POST.get('username')
		print username

        	password = request.POST.get('password')
        	print password
		user = authenticate(username=username, password=password)
		if user:
			
            		if user.is_active:
				print username,password
               			auth_login(request,user)
                		return redirect('/home')
            		else:
				return redirect('/?error=7')
        	else:
            		print "Invalid login details: {0}, {1}".format(username, password)
            		return redirect('/?error=6')
	else:
		return redirect('/')


### for registration		
def register(request):
	if request.user.is_authenticated():
		return redirect('/home')
	if request.method == 'POST':
		username = request.POST.get('username')
        	password = request.POST.get('password')
		email = request.POST.get('email')
        	conf_password = request.POST.get('confirm-password')
		if len(username) <6 or len(password)<6 :
			return redirect('/?error=0')
		if not username or not password or not email or not conf_password:
			return redirect('/?error=1')
		if password!= conf_password :
			return redirect('/?error=2')
		exist=True
		try :
			user_check=User.objects.get(username=username)
		except:
			exist=False
		if exist:
			return redirect('/?error=3')
		try :		
			email_check=User.objects.get(email=email)
		except:
			exist=False
		if exist:
			return redirect('/?error=4')
		role_type=request.POST.get('role')
		roll_id=request.POST.get('roll_id')
		print roll_id
		try:
			role=Role.objects.get(designation=role_type)
			role_int=role.role
			if role_int==1:
				exist=True
				try :
					user_check=Instructor.objects.get(i_id=roll_id)
				except:
					exist=False
				if exist:
					return redirect('/?error=8')
			if role_int==2:
				exist=True
				try :
					user_check=TA.objects.get(roll=roll_id)
				except:
					exist=False
				if exist:
					return redirect('/?error=8')
			if role_int==3:
				exist=True
				try :
					user_check=Student.objects.get(roll=roll_id)
				except:
					exist=False
				if exist:
					return redirect('/?error=8')
			new_user=User.objects.create_user(username=username,password=password,email=email)
			print new_user,"is"			
			new_user_profile=UserProfile.objects.create(user=new_user,role=role)
			print new_user_profile
			dept=Departments.objects.get(dep_id=0)
			print dept
			if role_int==1:
				print dept
				Instructor.objects.create(user=new_user_profile,i_id=roll_id,dept=dept)
				print "yahan"
			if role_int==2:
				TA.objects.create(user=new_user_profile,roll=roll_id,dept=dept)
			if role_int==3:
				Student.objects.create(user=new_user_profile,roll=roll_id,dept=dept)
		except:
			return redirect('/?error=5')
		user = authenticate(username=username, password=password)
		auth_login(request, user)
		return HttpResponseRedirect('/home/')
	else:
		return redirect('/')


##### for password recovery module
def recover(request):
	return HttpResponse("recover")

###### for logout
def logout(request):
	auth_logout(request)
	return redirect('/')


