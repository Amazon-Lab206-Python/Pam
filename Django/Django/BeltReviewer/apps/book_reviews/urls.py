from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^books/create_new$', views.create_new),
    url(r'^books/(?P<book_id>\d+)/add_new$', views.add_new),
    url(r'^books/(?P<book_id>\d+)$', views.book_info),
    url(r'^books/(?P<review_id>\d+)/delete$', views.destroy),
    url(r'^users/(?P<user_id>\d+)$', views.user_info),
]