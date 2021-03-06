#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from ZhiHuShowPage.models import QuestionInfo
from ZhiHuShowPage.models import Person
from django.contrib.messages.storage import session
from ZhiHuShowPage.models import PersonTopic
from ZhiHuShowPage.models import RecommendFollow
from ZhiHuShowPage.models import RecommendTopic
from ZhiHuShowPage.models import AucComplex
import json
from django.http.response import HttpResponse
from ZhiHuShowPage.models import TopicIdIntroduction
import random
from ZhiHuShowPage.models import Followees
from ZhiHuShowPage.models import Topicfollow
from ZhiHuShowPage.models import Answer
import time
from PIL import Image
import matplotlib.pyplot as plt
import os
from django.conf import settings
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
                    return redirect("/userIndex")
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
            return redirect('/userIndex')
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
#翻页的功能
def filter_by_questionId(request, dbName, questionId):
    
    ONE_PAGE_OF_DATA = 10 
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
    
    #filterDatas = dbName.objects.filter(questionid__exact = questionId)
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
    answers = filter_by_questionId(request, Answer, questionId)
    questionInfo = QuestionInfo.objects.filter(questionid__exact = questionId)
    if answers["allPage"] == 0:
        answers = QuestionInfo.objects.filter(questionid__exact = questionId)[0:1]
        
        return render_to_response("topic.html", {'answers':answers, 'allPage':0, 'curPage':0, 'answersCount':0, 'loginUser':loginUser, 'questionInfo':questionInfo[0]})
    return render_to_response("topic.html", {'answers':answers['datas'], 'allPage':answers["allPage"], 'curPage':answers["curPage"], 'loginUser':loginUser, 'questionInfo':questionInfo[0]})

#算法指标展示
def algorithmShow(request):
    loginUser = request.session.get("loginUser", "none")
    
    if request.method == "POST":
        
        val_name = request.POST.get('val_name', 'none')
        
        if  val_name == 'none'  or val_name == "":
            return render_to_response("algorithmShow.html", {"loginUser":loginUser})
        else:
            aucs = AucComplex.objects.filter(sim__exact = val_name)
            jsonData = {}
            param = []
            auc = []
            for p in aucs:
                param.append(p.param)
                auc.append(p.auc)
            jsonData['param'] = param
            jsonData['auc'] = auc
#            return render_to_response("algorithmShow.html", {"loginUser":loginUser, "aucs":aucs})
            return HttpResponse(json.dumps(jsonData), content_type = 'application/json')
#            return HttpResponse(auc)
    return render_to_response("algorithmShow.html", {"loginUser":loginUser})

#话题树展示
def topicTree(request):
    loginUser = request.session.get("loginUser", "none")
    return render_to_response("topicTree.html", {"loginUser":loginUser})

#话题树-复杂网络关系展示
def complexNet(request):
    loginUser = request.session.get("loginUser", "none")
    if request.method == "POST":
        userName = str(request.POST.get('userName', '王不二'))
        nets = Followees.objects.filter(personid__exact = userName)
        jsonData = {}
        nodes = []
        links = []
        
        nodeDir = {}
        nodeDir['category'] = 0
        nodeDir['name'] = nets[0].personid
        nodeDir['value'] = 30
        nodes.append(nodeDir)
        for net in nets:
            nodeDir = {}
            nodeDir['category'] = random.randint(1, 2)
            nodeDir['name'] = net.followeesid
            nodeDir['value'] = random.randint(1, 10)
            nodes.append(nodeDir)
            
            linkDir = {}
            linkDir['source'] = net.followeesid
            linkDir['target'] = net.personid
            linkDir['weight'] = random.randint(1, 30)
            linkDir['name'] = '关注'
            links.append(linkDir)
        
        jsonData['nodes'] = nodes
        jsonData['links'] = links
        return HttpResponse(json.dumps(jsonData), content_type = 'application/json')
    elif request.method == "GET":
        userName = str(request.GET.get('username', '王不二'))
        nets = Followees.objects.filter(personid__exact = userName)
        jsonData = {}
        nodes = []
        links = []
        nodeDir = {}
        nodeDir['category'] = 0
        nodeDir['name'] = userName
        nodeDir['value'] = 30
        nodes.append(nodeDir)
        for net in nets:
            nodeDir = {}
            nodeDir['category'] = random.randint(1, 2)
            nodeDir['name'] = net.followeesid
            nodeDir['value'] = random.randint(1, 10)
            nodes.append(nodeDir)
            
            linkDir = {}
            linkDir['source'] = net.followeesid
            linkDir['target'] = net.personid
            linkDir['weight'] = random.randint(1, 30)
            linkDir['name'] = '关注'
            links.append(linkDir)
        
        jsonData['nodes'] = nodes
        jsonData['links'] = links
        return render_to_response("complexNet.html", {"loginUser":loginUser, 'jsonData':json.dumps(jsonData)})
def userInfo(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        return redirect('/index')
    #得到登入用户关注的话题名字
    if loginUser != "none":
        topicFollows = Topicfollow.objects.filter(id_p__exact = loginUser.id)
    
    return render_to_response('userInfo.html', {"loginUser":loginUser, "topicFollows":topicFollows})
#跳转至用户个人中心
def userIndex(request):
    
    #获取登入用户
    loginUser = request.session.get("loginUser", "none")
    recommendFollows = []
    if loginUser == 'none':
        return redirect('/index')
    else:
        
        #得到登入用户关注的话题名字
        topicFollows = Topicfollow.objects.filter(id_p = loginUser.id)
        #根用户关注的话题显示提问内容
        loginUserTopic = []
        if len(topicFollows) > 0:
            #这里有待优化
            topicids = [topic.topicid for topic in topicFollows]
            if (topicids) > 10:
                for rand_id in range(10):
                    topic_id = random.choice(topicids)
                    getTopic = QuestionInfo.objects.filter(fromtopicname__exact = topic_id)
                    if len(getTopic) > 0:
                        
                        loginUserTopic.append(getTopic[0:1][0])
                    else:
                        continue
            else:
                for tid in topicids:
                    getTopic = QuestionInfo.objects.filter(fromtopicname__exact = tid)
                    loginUserTopic.append(getTopic[0:1][0])
        else:
            loginUserTopic = []
            
        #获取推荐好友
        recommendFollows = RecommendFollow.objects.filter(personid__exact = loginUser.id)
        #获取推荐的话题
        recommendTopics = RecommendTopic.objects.filter(personid__exact = loginUser.id)[0:10]
        jsonData = {}
        for follow in recommendFollows:
            data = []
            friendName = []
            userInfo = Person.objects.filter(personname__exact = follow.personname)
            data.append(userInfo[0].personname)
            data.append(userInfo[0].persongender)
            data.append(userInfo[0].personbiography)
            data.append(userInfo[0].personfollowersnum)
            data.append(userInfo[0].personanswersnum)
            data.append(userInfo[0].personpostsnum)
            
            friendName.append(follow.cn_0_name)
            friendName.append(follow.cn_1_name)
            friendName.append(follow.cn_2_name)
            friendName.append(follow.cn_3_name)
            friendName.append(follow.cn_4_name)
            friendName.append(follow.cn_5_name)
            friendName.append(follow.cn_6_name)
            friendName.append(follow.cn_7_name)
            friendName.append(follow.cn_8_name)
            friendName.append(follow.cn_9_name)
            
            jsonData[userInfo[0].personname] = [data, friendName]
            #person = [ Person.objects.filter(personname__exact = follow.personname)[0]  for follow in recommendFollows]
        topicJson = {}
        for topic in recommendTopics:
            
            data = []
            topicFriendName = []
            topicInfo = TopicIdIntroduction.objects.filter(id__exact = topic.retopic_id)
            data.append(topicInfo[0].topicname)
            data.append(topicInfo[0].topicintroduction)
            
            topicFriendName.append(topic.cn_0_name)
            topicFriendName.append(topic.cn_1_name)
            topicFriendName.append(topic.cn_2_name)
            topicFriendName.append(topic.cn_3_name)
            topicFriendName.append(topic.cn_4_name)
            topicFriendName.append(topic.cn_5_name)
            topicFriendName.append(topic.cn_6_name)
            topicFriendName.append(topic.cn_7_name)
            topicFriendName.append(topic.cn_8_name)
            topicFriendName.append(topic.cn_9_name)
            
            topicJson[topicInfo[0].topicname] = [data, topicFriendName]
        if request.method == "POST":
            followId = request.POST['followId']
            flag = request.POST['flag']
            followName = request.POST['followName']
            if followId == "":
                pass
            else:
                #得到topicID或者personID找到对应的id
                if flag == 'follow-person':
                    Followees(person_id = loginUser.id, personid = loginUser.personname, id_f = followId, followeesid = followName).save()
                    res = RecommendFollow.objects.filter(personid = loginUser.id, refollow_id = followId)
                    if len(res) == 1:
                        res.delete()
                    else:
                        print '删除关注的好友失败，查询数据超过2条'
                elif flag == 'follow-topic':
                    Topicfollow(id_p = loginUser.id, personid = loginUser.personname, id_t = followId, topicid = followName).save()
                    
                    res = RecommendTopic.objects.filter(personid = loginUser.id, retopic_id = followId)
                    if len(res) == 1:
                        res.delete()
                    else:
                        print '删除关注的话题失败，查询数据超过2条'
                    
                    
                
    return render_to_response("userIndex.html", {'loginUser':loginUser, 'topicFollows':topicFollows, 'loginUserTopic':loginUserTopic, 'recommendFollows':recommendFollows, 'recommendTopics':recommendTopics, 'followData':json.dumps(jsonData), 'topicJson':json.dumps(topicJson)})# 'person':json.dumps(person, cls = PersonEncoder)})


#返回关注的人
def followPerson(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        return redirect('/index')
    #得到登入用户关注的人
    if loginUser != "none":
        if request.method == "GET":
            peopleFollows = Followees.objects.filter(person_id__exact = loginUser.id)
            followed = []
            for follow in peopleFollows:
                followed.append([follow.id_f, follow.followeesid])
        else:
            id_f = request.POST.get('id_f')
            Followees.objects.filter(person_id__exact = loginUser.id, id_f__exacl = id_f)
        return HttpResponse(json.dumps(followed, ensure_ascii = False, encoding = 'utf-8'))
#返回关注的话题
def followTopic(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        return redirect('/index')
    #得到登入用户关注的人
    if loginUser != "none":
        if request.method == "GET":
            topicFollows = Topicfollow.objects.filter(id_p = loginUser.id)
            topics = []
            for topic in topicFollows:
                topics.append([topic.id_t, topic.topicid])
            
        return HttpResponse(json.dumps(topics, ensure_ascii = False, encoding = 'utf-8'))
     
     
#修改个人信息页面
def updateSelf(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        return redirect('/index')
    else:
        if request.method == "POST":
#            nickname = request.POST.get('nickname', 'none')
#            password = request.POST.get('password', 'none')
            nickname = request.POST['nickname']
            password = request.POST['password']
            
            if  nickname == "none" or password == "none" or nickname == "" or password == "":
                return  render_to_response('updateSelf.html', {'loginUser':loginUser})
            else:
                user = Person.objects.get(id = loginUser.id)
                user.personname = nickname
                user.password = password
                user.save()
                loginUser.personname = nickname
                loginUser.password = password
                #及时更新cookie
                request.session["loginUser"] = user
                return  render_to_response('updateSelf.html', {'loginUser':loginUser})
    return  render_to_response('updateSelf.html', {'loginUser':loginUser})
#删除关注好友和关注话题
def deleteFollows(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        return redirect('/login')
    else:
        if request.method == "POST":
            followId = request.POST['followId']
            flag = request.POST['flag']
            if followId == "":
                pass
                return HttpResponse(json.dumps('fail'))
            else:
                #得到topicID或者personID找到对应的id
                if flag == 'follow-person':
                    res = Followees.objects.filter(person_id = loginUser.id, id_f = followId)
                    if len(res) == 1:
                        res.delete()
                    else:
                        print '删除关注的话题失败，查询数据超过2条'
                elif flag == 'follow-topic':
                    
                    res = Topicfollow.objects.filter(id_p = loginUser.id, id_t = followId)
                    if len(res) == 1:
                        res.delete()
                    else:
                        print '删除关注的话题失败，查询数据超过2条'
                    
                return HttpResponse(json.dumps('ok'))
def searchName(request):
    if request.method == "POST":
        username = request.POST.get('username', '王不二')
        likeNames = Person.objects.filter(personname__contains = username)
        names = []
        for name in likeNames:
            names.append(name.personname)
        if len(names) > 9:
            names = names[0:8]
        
        return HttpResponse(json.dumps(names), content_type = 'application/json')
    else:
        return redirect('/index')

#上传头像
def uploadHeadImg(request):
    if request.method == "POST":
        loginUser = request.session.get("loginUser", "none")
        if loginUser == 'none':
            return redirect('/index')
        else:
            photo = request.FILES['photo']
            if photo:
                phototime = request.user.username + str(time.time()).split('.')[0]
                photo_last = str(photo).split('.')[-1]
                photoname = '/static/headImg/%s.%s' % (phototime, photo_last)
                img = Image.open(photo)
                img.save(os.path.dirname(__file__) + photoname)
                photoname = '..' + photoname
                print photoname
                count = Person.objects.filter(id = loginUser.id).update(headimg = photoname)
                if count:
                    # 设置一个session，然后跳转到对应的页面，此处简易写写
                    return redirect('/userInfo')              
                else:
                    return HttpResponse('上传失败')
     
            return HttpResponse('图片为空')
    else:
        return redirect('/index')
    
