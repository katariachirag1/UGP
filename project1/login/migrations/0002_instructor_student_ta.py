# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_id', models.CharField(max_length=24)),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll', models.CharField(max_length=24)),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll', models.CharField(max_length=24)),
                ('user', models.OneToOneField(to='login.UserProfile')),
            ],
        ),
    ]
