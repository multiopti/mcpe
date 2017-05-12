# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:09:24 2017

@author: gsanchez@usb.ve
"""

# multi-objective analysis

import numpy as np

def pltc(v1,v2): #classic partially less than
    lv1 = v1.size
    lv2 = v2.size
    
    if lv1 != lv2:
        print("\n Vector sizes not equal \n")
    else:
        P1 = np.zeros(lv1)
        P2 = np.zeros(lv1)
        for i in range(0,lv1):
            if v1[0,i] <= v2[0,i]:
                P1[i] = 1
            else:
                P1[i] = 0
                
            if v1[0,i] < v2[0,i]:
                P2[i] = 1
            else:
                P2[i] = 0
                
    if  all(P1) and any(P2):
        return 1
    else:
        return 0

class VectorSet:
    data = np.array([])
    dim = 0
    size = 0
    
    def add(self,V):
        if self.size == 0:
            self.data = V
            self.dim = len(V)
            self.size = 1
        else:
            self.data = np.append(self.data,V,axis = 0)
            self.size = self.size + 1
    
    def disp(self):
        print("\n")
        print(self.data)
        print("\n")
        print('Size= %d' %self.size)
        
    def plts(self,V): #classic partially less than set
        if self.size == 0:
            return 0
        else:
            result = 0
            for i in range(0,self.size):
                if pltc(V,self.data[i:i+1,:]):
                    result = 1
            return result

    