from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^wish$', views.wish),
    url(r'^session$', views.login_user),
    url(r'^logout$', views.logout),
    url(r'^user_wishes$', views.user_wishes),
    url(r'^items/(?P<id>\d+)$', views.item),
    url(r'^add_item$', views.add_item),
    url(r'^create$', views.create_item),
    url(r'^delete/(?P<id>\d+)$', views.delete_item),
    url(r'^list_add/(?P<id>\d+)$', views.list_add),
]
