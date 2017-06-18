#coding=UTF-8
'''
Created on Dec 15, 2016

@author: ZWT
'''


def insertDB_zhihu_data(list):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
#     try:
    SQL = "INSERT INTO cn_topic(PersonID,retopic_ID,count_cn,cn_0,cn_1,cn_2,cn_3,cn_4,cn_5,cn_6,cn_7,cn_8,cn_9)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Params = (list[0][0]+1,list[0][1]+1,list[1],list[2][0]+1,list[2][1]+1,list[2][2]+1,list[2][3]+1,list[2][4]+1,list[2][5]+1,list[2][6]+1,list[2][7]+1,list[2][8]+1,list[2][9]+1)
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

#     MatrixAdjacency_Net,MaxNodeNum = Initialize_Divide.Init(NetFile),delimiter=','
import similarity_indicators.CommonNeighbor


NetFile = u'Data/Followees.txt'
MatrixAdjacency_Net = Initialize.Initialize_UserItem(np.loadtxt(NetFile,delimiter=','))
# print MatrixAdjacency_Net.shape
# temp = np.diag(MatrixAdjacency_Net)
# print np.argwhere(temp != 0)
m=8
# for m in range(MatrixAdjacency_Net.shape[0]):
while m == 8:
    
    Array = MatrixAdjacency_Net[m]
    tempCN = []
    for n in range(MatrixAdjacency_Net.shape[0]):
        if m != n:
            tempArray = MatrixAdjacency_Net[n]
            CN_Array = Array * tempArray
            CN = np.argwhere(CN_Array != 0)
            CN.shape = (CN.shape[0])
            CN = list(CN)
            count_CN = len(CN)
            List_CN = [[m,n],count_CN,CN]
#             print List_CN
            tempCN.append(List_CN)
    m += 1
    tempCN = sorted(tempCN,key = lambda x:x[1],reverse = True)
    tempNUM = 0
    for i in range(len(tempCN)):
        if tempNUM < 10:
            if Array[tempCN[i][0][1]] == 0:
                print tempCN[i]
                if len(tempCN[i][2]) >= 10:  
#                     print tempCN[i]
#                     insertDB_zhihu_data(tempCN[i])
                    tempNUM += 1
        else:
            break



    
    


