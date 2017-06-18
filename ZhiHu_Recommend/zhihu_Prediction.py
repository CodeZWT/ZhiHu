#coding=UTF-8
'''
Created on 2016年12月8日

@author: ZWT
'''
import time
import os
import MySQLdb
import Initialize_Divide
import Evaluation_Indicators.AUC


import similarity_indicators.CommonNeighbor
import similarity_indicators.Salton
import similarity_indicators.Jaccard
import similarity_indicators.Sorenson
import similarity_indicators.HPI
import similarity_indicators.HDI
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.AA
import similarity_indicators.RA

# import similarity_indicators.LP
# import similarity_indicators.Katz
# 
# import similarity_indicators.ACT
# import similarity_indicators.Cos

startTime = time.clock()
#初始化训练测试集合

NetFile = u'Data/Topic.txt'
NetName = 'Topic'

     
print "\nLink Prediction_mixture start：\n"
TrainFile_Path = 'Data\\'+NetName+'\\Train.txt'
if os.path.exists(TrainFile_Path):
    Train_File = 'Data\\'+NetName+'\\Train.txt'
    Test_File = 'Data\\'+NetName+'\\Test.txt'
    MatrixAdjacency_Train,MatrixAdjacency_Test,MaxNodeNum = Initialize_Divide.Init2(Test_File, Train_File)
else:
    MatrixAdjacency_Net,MaxNodeNum = Initialize_Divide.Init(NetFile)
    MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize_Divide.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)


similarity_StartTime = time.clock()

AUC_List = []

for Method in range(11):
    if Method == 0:
#         print '----------SIM----------基于局部信息----------SIM----------'
        print '----------Cn----------'
        Matrix_similarity = similarity_indicators.CommonNeighbor.Cn(MatrixAdjacency_Train)
        print Matrix_similarity.shape
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 1:
        print '----------Salton----------'
        Matrix_similarity = similarity_indicators.Salton.Salton(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 2:
        print '----------Jaccard----------'
        Matrix_similarity = similarity_indicators.Jaccard.Jaccavrd(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 3:
        print '----------Sorenson----------'
        Matrix_similarity = similarity_indicators.Sorenson.Sorenson(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 4:
        print '----------HPI----------'
        Matrix_similarity = similarity_indicators.HPI.HPI(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 5:
        print '----------HDI----------'
        Matrix_similarity = similarity_indicators.HDI.HDI(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 6:
        print '----------LHN-1----------'
        Matrix_similarity = similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 7:
        print '----------AA----------'
        Matrix_similarity = similarity_indicators.AA.AA(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 8:
        print '----------RA----------'
        Matrix_similarity = similarity_indicators.RA.RA(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
    elif Method == 9:
        print '----------PA----------'
        Matrix_similarity = similarity_indicators.PA.PA(MatrixAdjacency_Train)
        AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
        AUC_List.append(AUC)
#     elif Method == 10:
#         print '----------SIM----------基于路径----------SIM----------'
#         print '----------LP----------'
#         Matrix_similarity = similarity_indicators.LP.LP(MatrixAdjacency_Train)
#         AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
#     elif Method == 11:
#         print '----------Katz----------'
#         Matrix_similarity = similarity_indicators.Katz.Katz(MatrixAdjacency_Train)
#         AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
#     elif Method == 12:
#         print '----------SIM----------基于随机游走----------SIM----------'
#         print '----------ACT----------'
#         Matrix_similarity = similarity_indicators.ACT.ACT(MatrixAdjacency_Train)
#         AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
#     elif Method == 13:
#         print '----------Cos----------'
#         Matrix_similarity = similarity_indicators.Cos.Cos(MatrixAdjacency_Train)
#         AUC = Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)
    else:
        print "Method Error!"
        
similarity_EndTime = time.clock()
print '----------！！----------'
print "All SimilarityTime: %f s" % (similarity_EndTime- similarity_StartTime)

# #计算auc
# Evaluation_Indicators.AUC.Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)

endTime = time.clock()
print "\nRunTime: %f s" % (endTime - startTime)

print AUC_List

def insertDB_zhihu_data(list):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
#     try:
    SQL = "INSERT INTO auc(ID,type,CN,Salton,Jaccard,Sorenson,HPI,HDI,LHN_I,AA,RA,PA)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    Params = ('2','topic',list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9])
    cursor.execute(SQL,Params)
    ZhiHu_DB.commit()
#     except:
#         ZhiHu_DB.rollback()
    ZhiHu_DB.close()
    print '存储完成\n'
    
insertDB_zhihu_data(AUC_List)
