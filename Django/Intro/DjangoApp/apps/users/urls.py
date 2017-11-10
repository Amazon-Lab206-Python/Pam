from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/new$', views.new_user),
    url(r'^/register$', views.new_user),
    url(r'^/login$', views.login),
]