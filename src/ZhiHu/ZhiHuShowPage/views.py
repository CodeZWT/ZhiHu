#coding:utf-8
from django.shortcuts import render, render_to_response
from ZhiHuShowPage.models import Question

#跳转到主页面
def index(reqest):
    
    findResult = find(reqest, Question)
    return render_to_response("index.html", {'questions':findResult['datas'], 'allPage':findResult["allPage"], 'curPage':findResult["curPage"]})
    
#跳转到登入页面
def login(reqest):
    
    return render_to_response("login.html")

#跳转到注册页面
def register(reqest):
    
    return render_to_response("register.html")

def find(reqest, dbName):
    
    ONE_PAGE_OF_DATA = 15 
    result = {}
    try:  
        curPage = int(reqest.GET.get('curPage', '1'))  
        allPage = int(reqest.GET.get('allPage', '1'))  
        pageType = str(reqest.GET.get('pageType', ''))  
    except ValueError:  
        curPage = 1  
        allPage = 1  
        pageType = ''  
  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1  
    elif pageType == 'lastDown':
        curPage = allPage
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA  
    datas = dbName.objects.all()[startPos:endPos]  
  
    if curPage == 1 and allPage == 1: #标记1  
        allPostCounts = dbName.objects.count()  
        allPage = allPostCounts / ONE_PAGE_OF_DATA  
        remainPost = allPostCounts % ONE_PAGE_OF_DATA  
        if remainPost > 0:  
            allPage += 1 
    
    result["datas"] = datas
    result["allPage"] = allPage
    result["curPage"] = curPage
    return result
