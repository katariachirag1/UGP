from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from login.models import Role
import time
from login.models import *
from course.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
import uuid

def index(request,course_name):
	if(len(course_name)==0):
		return index_without_course(request)
	course=""
	try:
		course=Courses.objects.get(course_id=course_name)
	except:
		return HttpResponse("Coure Cannot be found Now")
	context_dict = {'course_name':course_name.upper()}
	f=Announcements.objects.filter(course=course)
	x=[]
	for i in range(0,len(f)):
		x.append(f[i])
		x[i]=str(x[i])
	x.reverse()
	print x
	try:
		context_dict['tokens']=Token.objects.get(course=course)
	except:
		i1=1
	context_dict['announcements']=x
	try:
		if request.user.is_authenticated():
			context_dict['user_login']=True
			user_profile=UserProfile.objects.get(user=request.user)
			role=user_profile.role.role
			if role == 1:
				print "Instructor "
				context_dict['Instructor']=True
				context_dict['link']="/course/"+course_name.upper()+"/Announcements"
			if role == 3 :
				print "Student"
				context_dict['Student'] =False
				print "mari hai"
				student=Student.objects.get(user=user_profile)
				course=Courses.objects.filter(course_id=(course_name.upper()))[0]
				print student,course
				s=Course_Roll_Matching_Student.objects.filter(roll=student,course=course)
				if len(s)==0:
					context_dict['Student'] =True
			if role == 2 :
				print "TA"
				context_dict['Ta'] =False
				student=TA.objects.get(user=user_profile)
				course=Courses.objects.filter(course_id=(course_name.upper()))[0]
				print student,course
				s=Course_Roll_Matching_TA.objects.filter(roll=student,course=course)
				if len(s)==0:
					context_dict['Ta'] =True
		
		else:
			context_dict['user_login']=False
	except:
		context_dict['user_login']=False
	return render(request, 'course/course_view.html', context_dict)



@login_required
def register_course(request,course_name):
	user_profile=UserProfile.objects.get(user=request.user)
	role=user_profile.role.role
	if role == 2:
		ta=TA.objects.get(user=user_profile)
		print ta
		courses=Courses.objects.filter(course_id=(course_name.upper()))
		course=courses[0]
		s=Course_Roll_Matching_TA.objects.filter(roll=ta,course=course)
		if(len(s)!=0):
			return redirect("/home")
		try :
			match=Course_Roll_Matching_TA.objects.create(roll=ta,course=course)
		except:
			return HttpResponse("Can't register now")
		course.no_of_ta=course.no_of_ta+1
		course.save()
		return HttpResponseRedirect("/course/"+course_name+"/")
	
	student=Student.objects.get(user=user_profile)
	print student
	courses=Courses.objects.filter(course_id=(course_name.upper()))
	course=courses[0]
	s=Course_Roll_Matching_Student.objects.filter(roll=student,course=course)
	if(len(s)!=0):
		return redirect("/home")
	try :
		match=Course_Roll_Matching_Student.objects.create(roll=student,course=course)
	except:
		return HttpResponse("Can't register now")
	course.no_of_students=course.no_of_students+1
	course.save()
	return HttpResponseRedirect("/course/"+course_name+"/")


@login_required
def check_token(request,course_name):
	print course_name
	token=request.GET['token']
	courses=Courses.objects.filter(course_id=(course_name.upper()))
	course=courses[0]
	user_profile=UserProfile.objects.get(user=request.user)
	role=user_profile.role.role
	if role == 3:
		tok=Token.objects.filter(course=course)[0]
		tok=tok.token_student
		print tok,token
		if token == tok :
			return HttpResponseRedirect("/course/"+course_name+"/register")
		else :
			return HttpResponse("Failed")
	elif role == 2:
		tok=Token.objects.filter(course=course)[0]
		tok=tok.token_ta
		print tok,token
		if token == tok :
			return HttpResponseRedirect("/course/"+course_name+"/register")
		else :
			return HttpResponse("Failed")
		#Ta ke liye karna hai





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


@login_required
def create_course(request):
	course_id=request.POST.get("course_id").upper()
	course_name=request.POST.get("course_name").upper()
	quiz=request.POST.get('Quiz')
	ass=request.POST.get('Assignment')
	mid=request.POST.get('mid')
	end=request.POST.get('end')
	about=request.POST.get('About')
	user_profile=UserProfile.objects.get(user=request.user)
	instructor=Instructor.objects.get(user=user_profile)
	course=""
	str1=uuid.uuid1().hex
	str2=uuid.uuid1().hex
	try:
		course=Courses.objects.create(course_id=course_id,course_name=course_name,instructor=instructor,date_started=datetime.datetime.now().date())
	except:
		return HttpResponse("Apologies course cannot be constructed now")
	idx=len(Announcements.objects.all())+1
	idt=len(Token.objects.all())+1
	print idx,idt
	Token.objects.create(token_id=idt,instructor=instructor,course=course,token_student=str1,token_ta=str2,date=datetime.datetime.now().date())
	Announcements.objects.create(announcement_id=idx,instructor=instructor,course=course,announcement=about,date=datetime.datetime.now().date())
	link="/course/"+course_id
	return redirect(link)

@login_required
def Announce_submit(request,course_name):
	about=request.POST.get('content')
	print "here"
	print about
	user_profile=UserProfile.objects.get(user=request.user)
	instructor=Instructor.objects.get(user=user_profile)
	course=""
	try:
		course=Courses.objects.get(course_id=course_name)
	except:
		return HttpResponse("Coure Cannot be found Now")
	idx=len(Announcements.objects.all())+1
	print idx
	Announcements.objects.create(announcement_id=idx,instructor=instructor,course=course,announcement=about,date=datetime.datetime.now().date())
	link="/course/"+course_name
	return redirect(link)