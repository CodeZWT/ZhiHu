#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from ZhiHuShowPage.models import QuestionInfo
from ZhiHuShowPage.models import AnswerQuestion
from ZhiHuShowPage.models import Person
from django.contrib.messages.storage import session

#跳转到主页面
def index(request):
    loginUser = request.session.get("loginUser", "none")
    findResult = find(request, QuestionInfo)
    
    return render_to_response("index.html", { 'questions':findResult['datas'], 'allPage':findResult["allPage"], 'curPage':findResult["curPage"], 'loginUser':loginUser})
#跳转到登入页面
def login(request):
    if request.method == "POST":
        email = str(request.POST.get("email"))
        password = str(request.POST.get("password"))
        if email != ""and password != "":
#            loginUser = Person.objects.filter(personid__exact = email)
            try:
                loginUser = Person.objects.get(personid = email)
            except:
                loginError = "用户名不存在"
                return render_to_response("login.html", {'loginError':loginError})
            else: 
                if loginUser.password == password:
                    
                    request.session["loginUser"] = loginUser
                    return redirect("/person")
                else:
                    loginError = "密码错误"
                    return render_to_response("login.html", {'loginError':loginError})
    return render_to_response("login.html")
#注销动作
def logout(request):
    del request.session["loginUser"]  #删除session
    return redirect("/index")
#跳转到注册页面
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("user")
        password = request.POST.get("password")
        personname = request.POST.get("personName")
        try:
            Person.objects.get(personid = username)
            registerError = username + "用户名已经存在"
            return render_to_response("register.html", {'registerError':registerError})
        except:
            user = Person(personid = username, password = password, personhashid = email, personname = personname)
            user.save()
            
            request.session["loginUser"] = user
            return redirect('/person')
    return render_to_response("register.html")

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
#翻页的功能
def filter_by_questionId(request, dbName, questionId):
    
    ONE_PAGE_OF_DATA = 15 
    result = {}
    try:  
        curPage = int(request.GET.get('curPage', '1'))  
        allPage = int(request.GET.get('allPage', '1'))  
        pageType = str(request.GET.get('pageType', ''))
        
        if questionId == "None":
            questionId = str(request.GET.get('questionId', ''))
    except ValueError:  
        curPage = 1  
        allPage = 1  
        pageType = ''  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1  
    elif pageType == 'pageLast':
        curPage = allPage
    elif pageType == "pageFirst":
        curPage = 1
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA  
    
    
    filterDatas = dbName.objects.filter(questionid__exact = questionId)
    datas = filterDatas[startPos:endPos]
    if curPage == 1 and allPage == 1: #标记1  
        allPostCounts = len(filterDatas) 
        allPage = allPostCounts / ONE_PAGE_OF_DATA  
        remainPost = allPostCounts % ONE_PAGE_OF_DATA  
        if remainPost > 0:  
            allPage += 1 
    
    result["datas"] = datas
    result["allPage"] = allPage
    result["curPage"] = curPage
    return result
#跳转到问题详情页面
def topic(request):
    loginUser = request.session.get("loginUser", "none")
    questionId = str(request.GET.get('id'))
    answers = filter_by_questionId(request, AnswerQuestion, questionId)
    answersCount = answers["allPage"]*15
    return render_to_response("topic.html", {'answers':answers['datas'], 'allPage':answers["allPage"], 'curPage':answers["curPage"], 'answersCount':answersCount, 'loginUser':loginUser})

#算法指标展示
def algorithmShow(request):
    loginUser = request.session.get("loginUser", "none")
    return render_to_response("algorithmShow.html", {"loginUser":loginUser})

#话题树展示
def topicTree(request):
    loginUser = request.session.get("loginUser", "none")
    return render_to_response("topicTree.html", {"loginUser":loginUser})

#话题树-复杂网络关系展示
def complexNet(request):
    loginUser = request.session.get("loginUser", "none")
    return render_to_response("complexNet.html", {"loginUser":loginUser})

