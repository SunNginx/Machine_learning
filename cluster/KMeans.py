#!/usr/bin/env python

import numpy as np
from sklearn.cluster import KMeans

def loadData(path):
    retCityName = []
    retCityData = []
    with open(path) as f:
        content = f.readlines()
    for line in content:
        retCityName.append(line.split(',')[0])
        retCityData.append(line.split(',')[1:])

    print(retCityName)
    print(retCityData)
    return retCityName,retCityData


if __name__ == '__main__':

    CityName,CityData = loadData('E:\\Machine_learning\\Data\\31省市居民家庭消费水平-city.txt')
    km = KMeans(n_clusters=4)
    label = km.fit_predict(CityData) #计算聚类中心并预测每个样本的聚类索引。
    expenses = np.sum(km.cluster_centers_,axis=1) #聚类中心点的数值加和
    for data in km.cluster_centers_:
        print('data=',data)
        sum = 0
        for da in data:
            sum = sum + da
        print('sum=',sum)

    print('km=',km)
    print('label=',label)
    print('expenses=',expenses)
    print('CityName=',CityName)

    CityCluster = [[],[],[],[]]
    for i in range(len(CityName)):
        CityCluster[label[i]].append(CityName[i])

    for j in range(4):
        print('Expenses:%.2f' % expenses[j])
        print(CityCluster[j])

