# -*- coding: utf-8 -*-

import numpy as np
from random import randint

x = np.ones((12, 3))
i=0
while i<12:
    x[i, 1] = randint(4, 16)
    x[i, 2] = randint(60, 82)
    i += 1

Y = np.random.uniform(13.5, 18.6, (12, 1))
A = ((x.transpose()).dot(x))
A = np.linalg.inv(A)
A = A.dot((x.transpose()).dot(Y))
temp1 = np.zeros((12, 1))
temp2 = np.zeros((12, 1))
print(A)
second_Y = A[0]+A[1]*x[:, 1]+A[2]*x[:, 2]
print(second_Y)
print(Y)



