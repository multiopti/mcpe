# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:06:58 2016

@author: Gustavo
"""
import numpy as np
from control import *
import matplotlib.pyplot as plt

ndim = 2

A = [[0 , 1],[1 ,-1]]

B = [[1],[0]]

C = [1 , 0]

D = 0

Q0 = np.array([[1.0 , 0.0],[0.0 , 1.0]])

R0 = 1.0

NPar = 10

Kmat = np.zeros((NPar,ndim))
for k in range(0,NPar):
    Q = ((k)/100.0)*Q0
    R = R0 - ((k)/100.0)
    #print(Q)
    K, S, E = lqr(A, B, Q, R)
    Kmat[k,:] = K 

print(Kmat)
    