#coding:utf-8
from django.conf.urls import url, include
from django.contrib import admin
from ZhiHuShowPage import views, views2, adminViews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^register/', views.register, name = 'register'),
    url(r'^topic/$', views.topic, name = 'topic'),
    url(r'^logout/', views.logout, name = 'logout'),
    url(r'^algorithmShow/', views.algorithmShow, name = 'algorithmShow'),
    
    url(r'^topicTree/', views2.topicTree, name = 'topicTree'),
    url(r'^complexNet/', views.complexNet, name = 'complexNet'),
    url(r'^userInfo/', views.userInfo, name = 'userInfo'),
    
    
    url(r'^userIndex/$', views.userIndex, name = 'userIndex'),
    url(r'^like/', views2.like, name = 'like'),
     url(r'askQuestion/', views2.ask, name = 'ask'),
    url(r'answerQuestion/', views2.answer, name = 'answer'),
    url(r'^likeQuestion/', views2.likeQuestion, name = 'likeQuestion'),
    url(r'^searchQuestion/', views2.searchQuestion, name = 'searchQuestion'),
    
    url(r'followPerson/', views.followPerson, name = 'followPerson'),
    url(r'followTopic/', views.followTopic, name = 'followTopic'),
    url(r'updateSelf/', views.updateSelf, name = 'updateSelf'),
    
    #后台用户管理页面
    url(r'adminIndex/', adminViews.adminIndex, name = 'adminIndex'),
    url(r'users/', adminViews.users, name = 'users'),
    url(r'user/', adminViews.user, name = 'user'),
    url(r'sign_in/', adminViews.sign_in, name = 'sign_in'),
    url(r'sign_out/', adminViews.sign_out, name = 'sign_out'),
    url(r'deleteUser/', adminViews.deleteUser, name = 'deleteUser'),
    url(r'updateUser/', adminViews.updateUser, name = 'updateUser'),
    url(r'addUser/', adminViews.addUser, name = 'addUser'),
    url(r'error/$', adminViews.error, name = 'error'),
    url(r'calendar/', adminViews.calendar, name = 'calendar'),
    
    url(r'deleteFollows/', views.deleteFollows, name = 'deleteFollows'),
    url(r'searchName/', views.searchName, name = 'searchName'),
    
]
