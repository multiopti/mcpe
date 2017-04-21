# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:09:24 2017

@author: gsanchez@usb.ve
"""

# multi-objective analysis

import numpy as np

def pltc(v1,v2): #classic partially less than
    lv1 = len(v1)
    lv2 = len(v2)
    
    if lv1 != lv2:
        print("\n Vector sizes not equal \n")
    else:
        P1 = np.zeros(lv1)
        P2 = np.zeros(lv1)
        for i in range(0,lv1):
            if v1[i] <= v2[i]:
                P1[i] = 1
            else:
                P1[i] = 0
                
            if v1[i] < v2[i]:
                P2[i] = 1
            else:
                P2[i] = 0
                
    if  all(P1) and any(P2):
        return 1
    else:
        return 0
    