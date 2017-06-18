#coding=UTF-8
'''
Created on Dec 18, 2016

@author: ZWT
'''

def insertDB_zhihu_data(list):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
#     try:
    SQL = "INSERT INTO cn_topic_copy(PersonID,retopic_ID,cn_0,cn_1,cn_2,cn_3,cn_4,cn_5,cn_6,cn_7,cn_8,cn_9)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Params = (list[0]+1,list[1],list[2][0]+1,list[2][1]+1,list[2][2]+1,list[2][3]+1,list[2][4]+1,list[2][5]+1,list[2][6]+1,list[2][7]+1,list[2][8]+1,list[2][9]+1)
    cursor.execute(SQL,Params)
    ZhiHu_DB.commit()
    print '存储完成'
#     except:
#         ZhiHu_DB.rollback()
#         print 'error'+str(list[0][0])+str(list[0][1])
    ZhiHu_DB.close()
    

import os
import MySQLdb
import Initialize
import numpy as np
import Evaluation_Indicators.AUC

import similarity_indicators.CommonNeighbor

SocialFile = u'Data/followees.txt'
MatrixAdjacency_Social,Maxnode = Initialize.Initialize_Social(np.loadtxt(SocialFile,delimiter=','))
print MatrixAdjacency_Social.shape


NetFile = u'Data/Topic.txt'
MatrixAdjacency_Net = Initialize.Initialize_UserItem(np.loadtxt(NetFile,delimiter=','))
print MatrixAdjacency_Net.shape
T_MatrixAdjacency_Net = MatrixAdjacency_Net.T


degree_user = [sum(MatrixAdjacency_Net[i]) for i in range(len(MatrixAdjacency_Net))]
degree_item = [sum(T_MatrixAdjacency_Net[i]) for i in range(len(T_MatrixAdjacency_Net))]
 
# temp = np.argwhere((np.array(degree_item)) == 0)
# temp.shape = (len(np.argwhere((np.array(degree_item)) == 0)))
# print  temp
# data_list = []
# for i in temp:
# #     print i
#     data = [4400,i+1]
#     data_list.append(data)
# print data_list
# matrix = np.mat(data_list)
# print matrix
# print matrix.shape
# writeTrainFile(matrix)
diag_user = np.diag(degree_user)
print "user的度的对角矩阵计算："+str(diag_user.shape)
inv_diag_user = np.linalg.inv(diag_user)
print "user的度的对角矩阵求逆矩阵："+str(inv_diag_user.shape)
diag_item = np.diag(degree_item)
print "item的度的对角矩阵计算："+str(diag_item.shape)
inv_diag_item = np.linalg.inv(diag_item)
print "item的度的对角矩阵求逆矩阵："+str(inv_diag_item.shape)
   
ProbS_UserItem = np.dot(np.dot(np.dot(T_MatrixAdjacency_Net,inv_diag_user),MatrixAdjacency_Net),inv_diag_item)
print ProbS_UserItem.shape
print ProbS_UserItem[0]

print 'start'

for user in range(len(MatrixAdjacency_Net)):
    print 'User is :'+str(user) 
    tempWuZhi = np.dot(ProbS_UserItem,MatrixAdjacency_Net[user])
    
    QualityList = []
    for item in range(len(MatrixAdjacency_Net[user])):
        if (MatrixAdjacency_Net[user,item] == 0):
            QualityList.append([item,tempWuZhi[item],0])
        else:
            QualityList.append([item,tempWuZhi[item],1])
    QualityList = sorted(QualityList,key = lambda QualityList:QualityList[1],reverse = True)

    ReList = []
    for n in QualityList:
        if n[2] == 0:
            if len(ReList) < 11:
                ReList.append(n[0])
            else:
                break    
    print 'ReList: '+str(ReList)
    Follow = MatrixAdjacency_Social[user]
    userFollow = np.argwhere(Follow != 0)
    userFollow.shape = (len(np.argwhere(Follow != 0)))
    print 'userFollow: '+str(userFollow)
    for re in ReList:
        re_followList = []
#         print re
        for person in userFollow:
#             print person
            personTopic = MatrixAdjacency_Net[person]
            if personTopic[re] == 1:
                if len(re_followList) < 11:
                    re_followList.append(person)
                else:
                    break
        if len(re_followList) < 10:
            for i in range(10):
                re_followList.append(4399)
            re_followList = re_followList[0:10]
        re_reson = [user,re,re_followList]
        print 're_reason:' +str(re_reson)
        insertDB_zhihu_data(re_reson)


