#Genera datos sistema de sistema a lazo cerrado
#y grafica el Frente de Pareto Energia Error / Energia Control

# Importar módulos necesarios

import numpy as np
import matplotlib.pyplot as plt
import random

from scipy import signal
from control.matlab import *
from control import *
import scipy.linalg
from numpy import linalg as LA



sys = tf([0.02], [1, 0.6 ,0.08,0])

sysc = ss(sys)

A = sysc.A
B = -sysc.B

C = -sysc.C

D = sysc.D



#Transformacion

M = np.hstack((B,A*B,A*A*B))
W = np.matrix([[0.08,0.6,1],[0.6,1,0],[1,0,0]])

T = M*W
Tinv = LA.inv(T) 
A = Tinv*A*T
B = Tinv*B
B[2] = 0.02
C = C*T
C[0] = 1

Q0 = np.array([[1.0 , 0.0, 0.0],[0.0 , 1.0, 0.0],[0.0 , 0.0, 1.0]])

R0 = 1.0

NPar = 11
ndim = 3
Kmat = np.zeros((NPar-1,ndim))
for k in range(1,NPar):
    Q = ((k)/NPar)*Q0
    R = R0 - ((k)/NPar)
    #print(Q)
    K, S, E = lqr(A, B, Q, R)
    Kmat[k-1,:] = K 

#print(Kmat)

#print(sys1)


#print(sysd)

final_p = 3000
sampling_t = 1
#Kp = 1
#Ci = 1
#Cd = 0.5

A1 = 0.0082
A2 = 0.0067

B1 = 1.489
B2 = -0.5488

t = np.arange(0.0, final_p, sampling_t)

Ft = len(t)
u = np.zeros(Ft)
e = np.zeros(Ft)
r = signal.square(2 * np.pi * 0.002 * t)

Par = np.zeros((NPar-1,2))
for k in range(0,NPar):
    K = np.matrix(Kmat[k-1,0:3]) 
    sys1 = ss(A-B*K,B*K[0,0],C,D)
    t, yout, xout = forced_response(sys1, t, r)
    ei = r - yout
    eni = np.dot(ei,ei)
    Par[k-1,0] = eni
    u = -K*xout + K[0,0]*r
    usum = np.zeros(Ft)
    acum = 0.0
    for i in range(1,Ft):
        usum[i] = u[0,i] + acum
        acum = usum[i]
    usum = np.matrix(usum)
    udot = usum*usum.T
    Par[k-1,1] = udot[0,0]
    
    
y = np.zeros(Ft)
u = np.zeros(Ft)
e = np.zeros(Ft)
Kp =  1 + 0.5*signal.square(2*np.pi*0.001*t)  #vector de falla
Ci =  1 + 0.5*signal.square(2*np.pi*0.001*t)
Cd =  1 + 0.5*signal.square(2*np.pi*0.001*t)

for i in range(2,Ft):
    y[i] = B1*y[i-1] + B2*y[i-2] + A1*u[i-1]+ A2*u[i-2] + 0.1*random.uniform(-0.01,0.01)
    e[i] = r[i] - y[i]
    u[i] = u[i-1] + (Kp[i]+Ci[i]+Cd[i])*e[i]-(Kp[i]+2*Cd[i])*e[i-1]+Cd[i]*e[i-2]
    


en = np.dot(e,e)
un = np.dot(u,u)

plt.plot(Par[:,1],Par[:,0],'xk')
plt.plot(un,en,'or')

print('%g %g\n' % (en,un))

#
ofile = open("control7.dat", 'w')
#
for i in range(1,len(t)):
    ofile.write('%g %g %g %g \n' % (t[i],r[i],u[i],y[i]))
#    
ofile.close()