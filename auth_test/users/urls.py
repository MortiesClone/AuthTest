from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^$', log_in),
    url(r'^home', HomeView.as_view(), name="home"),
]