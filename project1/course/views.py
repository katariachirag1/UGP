from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from login.models import Role
from login.models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse


def index(request,course_name):
	if(len(course_name)==0):
		return index_without_course(request)
	context_dict = {'course_name':course_name.upper()}
	try:
		if request.user.is_authenticated():
			context_dict['user_login']=True
			user_profile=UserProfile.objects.get(user=request.user)
			role=user_profile.role.role
			if role == 3:
				print "Instructor "
				context_dict['Instructor']=True
		else:
			context_dict['user_login']=False
	except:
		context_dict['user_login']=False
	return render(request, 'course/course_view.html', context_dict)



def index_without_course(request):
	context_dict = {'course_name':"Course Builder"}
	try:
		if request.user.is_authenticated():
			context_dict['user_login']=True
		else:
			context_dict['user_login']=False
	except:
		context_dict['user_login']=False
	return render(request, 'course/index.html', context_dict)