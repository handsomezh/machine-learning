

# -*- coding: utf-8 -*-

 
import csv
import random
 
data_path="you file path"
k=1
 
# 读取数据
with open(data_path,'r') as file:
    reader=csv.DictReader(file)
    datas=[row for row in reader]
    # print("row=",format(data))
 
# 数据的分组
n=len(datas)//3
random.shuffle(datas)
test_set=datas[0:n]
train_set=datas[n:]
# print("train_set=",train_set)
# print("test_set",test_set)
 
#距离的选择
def distance(d1,d2):
    res=0
    for key in ("radius","texture","perimeter","area","smoothness","compactness","symmetry","fractal_dimension"):
        res+=(float(d1[key])-float(d2[key]))**2
    return res**0.5
 
#KNN的算法
"""data 这个是求解的数据，包括这个数据的所有的特征的数据"""
def KNN(data):
    #求距离
    res=[{"result":train['diagnosis_result'],"distance":distance(data,train)} for train in train_set]
    #进行排序
    sorted(res,key=lambda item:item['distance'])
    # print("res=", res)
    #取前面的K个
    res2=res[0:k]
    # print(res2)
    #来一个加权的平均的数
    result={'B':0,'M':0}
    #求解总的距离
    total_length=0
    for r in res2:
        total_length+=r['distance']
    for r in res2:
        result[r['result']]+=1-r['distance']/total_length#这里的是要么是B 或者是M  =单个的距离/总的距离
 
    if result['B']>result['M']:
        return 'B'
    else:
        return 'M'
 
#测试的阶段
correct=0
for test in test_set
    result=test['diagnosis_result']
    result2=KNN(test)
    if result==result2:
        correct+=1;
 
print(correct)
print(len(test_set))
print("准确率=",correct/len(test_set))
