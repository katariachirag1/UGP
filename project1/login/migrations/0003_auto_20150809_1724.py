# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_instructor_student_ta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dep_id', models.IntegerField(default=0)),
                ('dep_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='dept',
            field=models.ForeignKey(default=0, to='login.Departments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(default=0, to='login.Departments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ta',
            name='dept',
            field=models.ForeignKey(default=0, to='login.Departments'),
            preserve_default=False,
        ),
    ]
