# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150809_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('announcement_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('announcement', models.TextField()),
                ('date', models.DateTimeField(verbose_name=b'Date Of Announcement')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('comment', models.TextField()),
                ('no_of_replies', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'Comment Date')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Roll_Matching_Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Roll_Matching_TA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=255)),
                ('no_of_students', models.IntegerField(default=0)),
                ('no_of_ta', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(verbose_name=b'Date Started')),
                ('instructor', models.ForeignKey(to='login.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('reply_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('reply', models.TextField()),
                ('date', models.DateTimeField(verbose_name=b'Comment Date')),
                ('comment', models.ForeignKey(to='course.Comments')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('token_student', models.CharField(max_length=1024)),
                ('token_ta', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(verbose_name=b'Token Created')),
                ('course', models.ForeignKey(to='course.Courses')),
                ('instructor', models.ForeignKey(to='login.Instructor')),
            ],
        ),
        migrations.AddField(
            model_name='course_roll_matching_ta',
            name='course',
            field=models.ForeignKey(to='course.Courses'),
        ),
        migrations.AddField(
            model_name='course_roll_matching_ta',
            name='roll',
            field=models.ForeignKey(to='login.TA'),
        ),
        migrations.AddField(
            model_name='course_roll_matching_student',
            name='course',
            field=models.ForeignKey(to='course.Courses'),
        ),
        migrations.AddField(
            model_name='course_roll_matching_student',
            name='roll',
            field=models.ForeignKey(to='login.Student'),
        ),
        migrations.AddField(
            model_name='comments',
            name='course',
            field=models.ForeignKey(to='course.Courses'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
        ),
        migrations.AddField(
            model_name='announcements',
            name='course',
            field=models.ForeignKey(to='course.Courses'),
        ),
        migrations.AddField(
            model_name='announcements',
            name='instructor',
            field=models.ForeignKey(to='login.Instructor'),
        ),
    ]
