from django.contrib import admin

from .models import Courses

admin.site.register(Courses)

from .models import Announcements

admin.site.register(Announcements)

from .models import Comments

admin.site.register(Comments)

from .models import Reply

admin.site.register(Reply)


from .models import Token

admin.site.register(Token)


from .models import Course_Roll_Matching_Student

admin.site.register(Course_Roll_Matching_Student)


from .models import Course_Roll_Matching_TA

admin.site.register(Course_Roll_Matching_TA)

