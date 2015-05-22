from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'user/login$', views.login),
    url(r'user/logout$', views.logout),
)
