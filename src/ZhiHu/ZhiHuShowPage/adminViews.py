#coding=UTF-8
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.storage import session
from ZhiHuShowPage.models import Person, Topicfollow, TopicIdIntroduction
import json
from ZhiHuShowPage.models import Topic, TopicId
import numpy
from django.http.response import HttpResponse
from ZhiHuShowPage.models import QuestionInfo

#跳转至用户管理后台中心
def adminIndex(request):
    
    adminUser = request.session.get("adminUser", "none")
    if adminUser == 'none':
        return redirect("/sign_in")
    else:
        users = Person.objects.order_by('-id')[0:10]
        userCount = Person.objects.all().count()
        topicCount = TopicId.objects.all().count()
        questionCount = QuestionInfo.objects.all().count()
        counts = {}
        counts['userCount'] = userCount
        counts['topicCount'] = topicCount
        counts['questionCount'] = questionCount
        return render_to_response("admins/index.html", {"users":users, 'adminUser':adminUser, 'counts':counts})

#跳转至所有用户管理
def users(request):
    adminUser = request.session.get("adminUser", "none")
    if adminUser == 'none':
        return redirect("/sign_in")
    else:
        users = find(request, Person)
        return render_to_response("admins/users.html", {"users":users['datas'], 'allPage':users["allPage"], 'curPage':users["curPage"], 'adminUser':adminUser})

#跳转个体用户管理
def user(request):
    adminUser = request.session.get("adminUser", "none")
    if adminUser == 'none':
        
        
        return redirect("/sign_in")
    else:
        userId = int(request.GET.get('id', -1))
        print userId
        if userId == -1:
            #默认找到admin的资料
            user = Person.objects.get(id = adminUser.id)
            return render_to_response("admins/user.html", {'user':user, 'adminUser':adminUser})
        else:
            
            user = Person.objects.get(id = userId)
            return render_to_response("admins/user.html", {'user':user, 'adminUser':adminUser})

#跳转登入
def sign_in(request):
    
    if request.method == "POST":
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        print username, password
        if username != ""and password != "" and username == "admin":
            try:
                adminUser = Person.objects.get(personid = username)
            except:
                loginError = "用户名不存在"
                return render_to_response("admins/sign-in.html", {'loginError':loginError})
            else: 
                if adminUser.password == password:
                    request.session["adminUser"] = adminUser
                    return redirect("/adminIndex")
                else:
                    loginError = "密码错误"
                    return render_to_response("admins/sign-in.html", {'loginError':loginError})
    return render_to_response("admins/sign-in.html")

#退出登入
def sign_out(request):
    del request.session["adminUser"]  #删除session
    return redirect("/sign_in")

#翻页的功能
def find(request, dbName):
    
    ONE_PAGE_OF_DATA = 15 
    result = {}
    try:  
        curPage = int(request.GET.get('curPage', '1'))  
        allPage = int(request.GET.get('allPage', '1'))  
        pageType = str(request.GET.get('pageType', ''))  
    except ValueError:  
        curPage = 1  
        allPage = 1  
        pageType = ''  
  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1  
    elif pageType == 'pageFirst':
        curPage = 1
    elif pageType == 'pagelast':
        curPage = allPage   
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA  
    #datas = dbName.objects.all()[startPos:endPos]  
    datas = dbName.objects.order_by('-id')[startPos:endPos]
  
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
def deleteUser(request):
    if request.method == "POST":
        userId = int(request.POST.get('id', 0))
        if userId == 0:
            pass
        else:
            Person.objects.get(id = userId).delete()
            
            return redirect("/users")
    else:
        return redirect('/users')
        
def updateUser(request):
    if request.method == "POST":
        username = request.POST['username']
        nickname = request.POST['nickname']
        password = request.POST['password']
        biography = request.POST['biography']
        address = request.POST['address']
        business = request.POST['business']
        if username == "" or nickname == '' or password == "":
            return redirect("/users")
        else:
            user = Person.objects.get(personid = username)
            user.personname = nickname
            user.password = password
            user.personbiography = biography
            user.personaddress = address
            user.personbusiness = business
            user.save()
            return redirect("/users")
    else:
        return redirect('/user')
def addUser(request):
    if request.method == "POST":
        username = request.POST['username']
        nickname = request.POST['nickname']
        password = request.POST['password']
        biography = request.POST['biography']
        address = request.POST['address']
        business = request.POST['business']
        if username == "" or nickname == '' or password == "":
            
            return redirect('/users')
        else:
            u = Person.objects.filter(personid__exact = username)
            if len(u) > 0:
                print username
                print '用户名已经存在'
                errorMsg = "用户名已经存在"
                return HttpResponse(json.dumps(errorMsg), content_type = 'application/json')
            else:
                print 2
                user = Person()
                user.personid = username
                user.personname = nickname
                user.password = password
                user.personbiography = biography
                user.personaddress = address
                user.personbusiness = business
                user.save()
            
            return redirect('/users')
    else:
        return redirect('/user')
    
def error(request):
    adminUser = request.session.get("adminUser", "none")
    if adminUser == 'none':
        return redirect("/sign_in")
    else:
        page = request.GET.get('pageInfo', '404')
        
        return render_to_response("admins/" + page + ".html", {'adminUser':adminUser })
def calendar(request):
    adminUser = request.session.get("adminUser", "none")
    if adminUser == 'none':
        return redirect("/sign_in")
    else:
        
        return render_to_response("admins/calendar.html", {'adminUser':adminUser })
