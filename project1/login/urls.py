from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recover/',views.register,name='recover'),
    url(r'^$', views.index, name='index'),
    
]
