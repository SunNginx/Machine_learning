#!/usr/bin/env python

import numpy as np

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
iris_data = load_iris() #加载数据集


x_axis = iris_data.data[:,0] #第一列
len_x = len(x_axis)
y_axis = iris_data.data[:,2] #第三列
len_y = len(y_axis)


#分类数
model = KMeans(n_clusters=3)
#训练模型
model.fit(iris_data.data)


prddicted_label= model.predict([[6.3, 3.3, 6, 2.5]]) #选取行标为100的那条数据，进行预测,看看是哪一类的
prddicted_label1= model.predict([iris_data.data[1]]) #看第一行数据是哪一类

#预测全部150条数据
all_predictions = model.predict(iris_data.data) #predict ，预测iris_data.data中每个样本所属的最近集群

expenses = np.sum(model.cluster_centers_,axis=1) #聚类中心点的和
result =[[],[],[]] #记录每一类，所对应的样本值
for i in range(len(all_predictions)):
    result[all_predictions[i]].append(iris_data.data[i])
for j in range(len(expenses)):
    print(expenses[j])
    print(result[j])
#看看x,y,对应的点，对应不同类就是不同颜色，用散点图直观
plt.scatter(x_axis,y_axis,c = all_predictions)
plt.show()


