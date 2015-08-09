from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from login.models import *
# Create your models here.


class Courses(models.Model):
	course_id = models.CharField(max_length=20, primary_key=True )
	course_name = models.CharField(max_length=255)
	instructor = models.ForeignKey(Instructor)
	no_of_students = models.IntegerField(default=0)
	no_of_ta = models.IntegerField(default=0)
	date_started = models.DateTimeField('Date Started')
	def __unicode__(self):
		return self.course_name

class Announcements(models.Model):
	announcement_id = models.IntegerField(default=0, primary_key=True )
	course = models.ForeignKey(Courses)
	instructor = models.ForeignKey(Instructor)
	announcement = models.TextField()
	date = models.DateTimeField('Date Of Announcement')
	def __unicode__(self):
		return self.announcement


class Comments(models.Model):
	comment_id = models.IntegerField(default=0, primary_key=True )
	user = models.ForeignKey(UserProfile)
	comment = models.TextField()
	no_of_replies = models.IntegerField(default=0)
	date = models.DateTimeField('Comment Date')
	course = models.ForeignKey(Courses)
	def __unicode__(self):
		return self.comment

class Reply(models.Model):
	reply_id = models.IntegerField(default=0, primary_key=True )
	user = models.ForeignKey(UserProfile)
	reply = models.TextField()
	comment = models.ForeignKey(Comments)
	date = models.DateTimeField('Comment Date')
	def __unicode__(self):
		return self.reply

class Token(models.Model):
	token_id = models.IntegerField(default=0, primary_key=True )
	token_student = models.CharField(max_length=1024)
	token_ta = models.CharField(max_length=1024)
	course = models.ForeignKey(Courses)
	instructor = models.ForeignKey(Instructor)
	date = models.DateTimeField('Token Created')
	def __unicode__(self):
		return self.token_id


class Course_Roll_Matching_Student(models.Model):
	roll = models.ForeignKey(Student)
	course = models.ForeignKey(Courses)
	def __unicode__(self):
		return self.roll


class Course_Roll_Matching_TA(models.Model):
	roll = models.ForeignKey(TA)
	course = models.ForeignKey(Courses)
	def __unicode__(self):
		return self.roll
		