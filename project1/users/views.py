from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from login.models import Role
from login.models import UserProfile
from login.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
## index view

@login_required
def index(request):
    context_dict = {}
    role=UserProfile.objects.get(user=request.user).role.role
    context_dict['role']=role
    print role
    if role==1:
    	return render(request, 'user/Instructor.html', context_dict)
    if role==2:
    	return render(request, 'user/TA.html', context_dict)
    if role==3:
    	return render(request, 'user/Student.html', context_dict)




