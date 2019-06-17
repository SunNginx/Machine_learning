#!/usr/bin/env python
import numpy as np

default = np.sum([[0, 1], [0, 5]])
axis_0 = np.sum([[0, 1], [0, 5]], axis=0)
axis_1 = np.sum([[0, 1], [0, 5]], axis=1)
# axis_2 = np.sum([[0, 1], [0, 5]], axis=2)
dtype_32 = np.sum([[0, 1], [0, 5]], dtype=np.int32)
print(default)
print(axis_0)
print(axis_1)
# print('axis_2=',axis_2)
print('dtype_32=',dtype_32)