from django.urls import path
from Profiler.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'Profiler'

urlpatterns = [
    url(r'add_student/$',add_student),
    url(r'add_dept/$',add_dept, name='add_dept'),
    url(r'control_panel/$',control_panel),
    url(r'departments/$',departments),
    url(r'address/$',address),
    url(r'add_add/$',add_address,name='add_address'),
    url(r'^dept/(?P<name>\w+)/update/$',dept_update, name='dept_update'),
    #url(r'^addr/(?P<street>\w+)/update/$',address_update, name='address_update'),
]