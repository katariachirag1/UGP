# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150809_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='id',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='departments',
            name='dep_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='i_id',
            field=models.CharField(max_length=24, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=24, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ta',
            name='roll',
            field=models.CharField(max_length=24, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
