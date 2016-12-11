#coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from ZhiHuShowPage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
]
