from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^$', 'users.views.login'),
    url(r'^logout/', 'users.views.logout'),
]