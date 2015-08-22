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

def index(request):
	context_dict = {}
	return render(request, 'course/index.html', context_dict)