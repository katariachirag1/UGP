from django.contrib import admin

# Register your models here.
from .models import Student

admin.site.register(Student)

from .models import UserProfile

admin.site.register(UserProfile)

from .models import Role

admin.site.register(Role)

from .models import Departments

admin.site.register(Departments)

from .models import TA

admin.site.register(TA)

from .models import Instructor

admin.site.register(Instructor)

