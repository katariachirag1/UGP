from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views
from course import views as course_views
from users import views as user_views

urlpatterns = [
    url(r'^login',login_views.login),
    url(r'^logout',login_views.logout),
    url(r'^register',login_views.register),
    url(r'^recover',login_views.recover),
    url(r'^$', include('login.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',include('users.urls')),
    url(r'^user/',user_views.index),
    url(r'^course/create',course_views.create_course),
    url(r'^course/(?P<course_name>[\w\-]*)/check_token',course_views.check_token),
    url(r'^course/(?P<course_name>[\w\-]*)/register',course_views.register_course),
    url(r'^course/(?P<course_name>[\w\-]*)/Announcements',course_views.Announce_submit),
    url(r'^course/(?P<course_name>[\w\-]*)',course_views.index),
    
]
