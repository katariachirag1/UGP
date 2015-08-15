from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.template import RequestContext, loader


def index(request):
    latest_question_list = Student.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'login/index.html', context)
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)