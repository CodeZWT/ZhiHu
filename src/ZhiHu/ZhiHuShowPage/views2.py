#coding=UTF-8
'''
Created on Dec 13, 2016

@author: ZWT
'''
#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.storage import session
from ZhiHuShowPage.models import Question, Person, Topicfollow, TopicIdIntroduction



#跳转至用户个人中心
def person(request):
    #获取登入用户
    User = request.session.get("loginUser", "none")
    
    if User == 'none':
        return redirect('/index')
    
    tempperson = Person.objects.get(id = User.id)
    followTopic_list = Topicfollow.objects.filter(id_p = tempperson.id)
    topic_list = []
    for topic in followTopic_list:
        id = topic.topicid
        topicname = TopicIdIntroduction.objects.get(topicid = id)
        topic_list.append(topicname)
    topic_list = set(topic_list)
    return render_to_response("person.html", {'person':tempperson, 'followTopic':topic_list, 'loginUser':User})
