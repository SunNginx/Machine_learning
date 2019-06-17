#!/usr/bin/env python

from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape) #数据维度,多少行，多少列
data,target = load_boston(return_X_y=True) #为true表示返回target，默认为false，即只返回data
print(data.shape)
print(target.shape)