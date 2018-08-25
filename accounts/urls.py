from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^signup/$', views.signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
url(r'^login/$', views.user_login, name='first'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^',views.homepage,name='homepage'),
]
