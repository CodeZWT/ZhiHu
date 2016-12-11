#coding:utf-8
from django.shortcuts import render, render_to_response
from ZhiHuShowPage.models import Question

#跳转到主页面
def index(reqest):
    
    questions = Question.objects.all()[0:10]
    return render_to_response("index.html", {'questions':questions})

#跳转到登入页面
def login(reqest):
    
    return render_to_response("login.html")

#跳转到注册页面
def register(reqest):
    
    return render_to_response("register.html")
