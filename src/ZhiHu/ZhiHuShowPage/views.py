#coding:utf-8
from django.shortcuts import render, render_to_response

#跳转到主页面
def index(reqest):
    
    return render_to_response("index.html")
