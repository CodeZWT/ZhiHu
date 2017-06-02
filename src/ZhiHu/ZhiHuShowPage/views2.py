#coding=UTF-8
'''
Created on Dec 13, 2016

@author: ZWT
'''
#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.storage import session
from ZhiHuShowPage.models import  Person, Topicfollow, TopicIdIntroduction
import json
from ZhiHuShowPage.models import Topic, TopicId
import numpy

from django.http.response import HttpResponse
from ZhiHuShowPage.models import QuestionInfo
from ZhiHuShowPage.models import Answer

#跳转至用户个人中心
def userIndex(request):
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
    return render_to_response("userIndex.html", {'person':tempperson, 'followTopic':topic_list, 'loginUser':User})
def topicTree(request):
    def rangeRandom(constMinRadius, constMaxRadius):
        return numpy.random.random() * (constMaxRadius - constMinRadius) + constMinRadius 
    def Tree(TopicName):
        Nodes = []
        Links = []
        if TopicId.objects.filter(topicname = TopicName):            
            grandFatherObject = TopicId.objects.get(topicname = TopicName)
            RootNode = {'name':grandFatherObject.topicname,
                        'value':rangeRandom(25, 30),
                        'id':0,
                        'depth':0,
                        'category':2}
            Nodes.append(RootNode)
            #将第一层root节点存入Nodes
            father_list = Topic.objects.filter(father_topic_id = grandFatherObject.topicid)
    
            for Node_F in father_list:
                FatherNode = {'name':Node_F.child_topic,
                        'value':rangeRandom(20, 25),
                        'id':len(Nodes),
                        'depth':1,
                        'category':1}
                Nodes.append(FatherNode)
                Links.append({'source':RootNode["id"],
                              'target':FatherNode["id"],
                              'weight':1})
                #将第二层的节点存入
                son_list = Topic.objects.filter(father_topic_id = Node_F.child_topic_id)
    
                for Node_S in son_list:
                    SonNode = {'name':Node_S.child_topic,
                        'value':rangeRandom(15, 20),
                        'id':len(Nodes),
                        'depth':2,
                        'category':0}
                    Nodes.append(SonNode)
                    Links.append({'source':FatherNode["id"],
                                  'target':SonNode["id"],
                                  'weight':1
                        })
                    #第三层节点存入    
        else:
            print 'No Child'
            Nodes, Links = Tree('【根话题】')
        return Nodes, Links 
    
    loginUser = request.session.get("loginUser", "none")
    if request.method == 'POST':
        TopicName = request.POST.get('TopicName', 'none')
        if  TopicName == 'none'  or TopicName == "":
            return render_to_response("topicTree.html", {"loginUser":loginUser})
        else:
            
            print 'post'
            print TopicName
            Nodes, Links = Tree(TopicName)
            print json.dumps(Nodes[0], ensure_ascii = False, encoding = 'utf-8')
            Data = {'Nodes':Nodes, 'Links':Links}
            return HttpResponse(json.dumps(Data), content_type = 'application/json')
    

    return render_to_response("topicTree.html", {"loginUser":loginUser})




def like(request):
    if request.method == 'POST':
        print 'post'
        key = request.POST.get('inputText')
        print 'key:' + json.dumps(key, ensure_ascii = False, encoding = 'utf-8')
        keyWords = TopicId.objects.filter(topicname__contains = key)
        data = []
        for i in keyWords:
            data.append(i.topicname)
        if len(data) > 5:
            data = data[0:5]
        print json.dumps(data, ensure_ascii = False, encoding = 'utf-8')
        return HttpResponse(json.dumps(data))
    else:
        print 'get'
        data = ['error']
        return HttpResponse(data)
    
def ask(request):
    if request.method == 'POST':
        print 'post'
        QuestionText = request.POST.get('inputText')
        fromTopicName = request.POST.get('topicName')
        try:
            fromTopicId = TopicId.objects.get(topicname = fromTopicName).topicid
        except:
            print "没有输入话题"
        maxQuestionID = QuestionInfo.objects.latest('questionid').questionid
        print maxQuestionID
        newQuestion = QuestionInfo()
        newQuestion.questionid = int(maxQuestionID) + 1
        newQuestion.questionname = QuestionText
        newQuestion.fromtopicid = fromTopicId
        newQuestion.fromtopicname = fromTopicName
        newQuestion.save()
        return HttpResponse('Success')
def answer(request):
    if request.method == 'POST':
        answerID = request.POST.get('answerId')
        userID = request.POST.get('userId')
        Text = request.POST.get('Text')
        questionID = request.POST.get('questionID')
        print answerID, userID, Text, questionID
        question = QuestionInfo.objects.filter(questionid = questionID)
#         print question[0].questionname
#         print question[0].questionid
        questionID = question[0].questionid
        maxAnswerID = Answer.objects.latest('answerid').answerid
        personID = Person.objects.get(id = userID).personid
        answerQuestion = Answer()
        answerQuestion.questionid = questionID
        answerQuestion.personid = personID
        answerQuestion.answerid = int(maxAnswerID) + 1
        answerQuestion.content = Text
        answerQuestion.save()
        print int(maxAnswerID) + 1
        return HttpResponse('Success')


def likeQuestion(request):
    if request.method == 'POST':
        print 'post'
        key = request.POST.get('inputText')
        print 'key:' + json.dumps(key, ensure_ascii = False, encoding = 'utf-8')
        questions = QuestionInfo.objects.filter(questionname__contains = key)
        data = []
        for i in questions:
            data.append(i.questionname)
        data = list(set(data))
        if len(data) > 5:
            data = data[0:5]
        print json.dumps(data, ensure_ascii = False, encoding = 'utf-8')
        return HttpResponse(json.dumps(data))
    else:
        print 'get'
        data = ['error']
        return HttpResponse(data)
def searchQuestion(request):
    loginUser = request.session.get("loginUser", "none")
    if request.method == 'POST':
        print 'post'
        QuestionText = request.POST.get('inputText')
        questions = QuestionInfo.objects.filter(questionname__contains = QuestionText)
        
        questionId = questions[0].questionid
        print  QuestionText, len(questions), questionId
        return HttpResponse(json.dumps(questionId))
#         answers = views.filter_by_questionId(request, AnswerQuestion, questionId)
#         answersCount = answers["allPage"]*15
#         #print questionId,answers['datas'][0].answerid,answers['datas'][0].personid,answers['datas'][0].questionname,answers['datas'][0].fromtopicname
#         return render_to_response("topic.html", {'answers':answers['datas'], 'allPage':answers["allPage"], 'curPage':answers["curPage"], 'answersCount':answersCount, 'loginUser':loginUser})
