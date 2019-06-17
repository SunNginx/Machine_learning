#!/usr/bin/env python

from sklearn.datasets import load_iris

print(load_iris().data.shape)
data,target = load_iris(return_X_y=True)