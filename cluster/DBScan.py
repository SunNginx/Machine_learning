#!/usr/bin/env python
#上网时长和上网时间的聚类分析


import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt

mac2id = dict()
onlinetimes = []
f = open('E:\\Machine_learning\\Data\\学生月上网时间分布-TestData.txt', encoding='utf-8')
for line in f:
    mac = line.split(',')[2]
    onlinetime = int(line.split(',')[6])
    starttime = int(line.split(',')[4].split(' ')[1].split(':')[0])
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime, onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime, onlinetime)]

real_X = np.array(onlinetimes).reshape((-1, 2)) #将list类型的online

#开始对上网开始时间进行DBSCAN聚类分析
X = real_X[:, 0:1]#上网开始时间的list

db = skc.DBSCAN(eps=0.01, min_samples=20).fit(X) #用DBSCAN聚类算法分析开始上网时间，X为上网开始时间list
labels = db.labels_  #每个样本的簇类0，1,2,3,4,5，-1，-1为噪音点，

print('Labels:')
print(labels)
raito = len(labels[labels[:] == -1]) / len(labels) #labels[:] == -1判断每个样本的label是否等于-1，若等于则为噪音点，labels[labels[:] == -1]取labels中所有噪音点，求其len，就是看有多少个噪音点。除以标签的总长。则raito为噪音点的比率
print('Noise raito:', format(raito, '.2%'))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0) #set(labels)取一个label中的无需不重复集合，即簇个数包含噪音点

print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels)) #sklearn.metrics.silhouette_score：计算所有样本的平均轮廓系数

for i in range(n_clusters_):
    print('Cluster ', i, ':')
    print(list(X[labels == i].flatten()))
    #numpy中的flatten()函数，可以返回一个一维数组，a.flatten()：a是个数组，a.flatten()就是把a降到一维，默认是按行的方向降 。
    #flatten只能适用于numpy对象，即array或者mat，普通的list列表不适用！。

# plt.hist(X, 24) #hist画直方图
# plt.show()

#开始对上网时长进行聚类分析
#DBSCAN
y = real_X[:,1:2]
db_y = skc.DBSCAN(eps=0.1,min_samples=10).fit(y)
labels_y = db_y.labels_
print('labels:')
print(labels_y)
#KMeans
km = skc.KMeans(n_clusters=4)
label_k = km.fit_predict(y)
expensens = np.sum(km.cluster_centers_,axis=1)
for i in range(4):
    print('cluster '+ str(i) +':')
    print('expensens :',expensens[i])
    temp = list(y[label_k == i].flatten())
    print(temp)

xaxis = X.flatten()
yaxis = y.flatten()
plt.scatter(yaxis,xaxis,c=label_k)
plt.show()

