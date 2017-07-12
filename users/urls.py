from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^logout/', logout),
]
