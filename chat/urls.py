from django.conf.urls import url

from . import views

app_name = "chat"

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_submit/$', views.login_submit, name='login_submit'),
]
