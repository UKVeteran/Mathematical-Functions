from random import uniform as u
from matplotlib import pyplot as plt

def f(x): return x**3 +3/4 * x**2 +x/2 +1

lower =1 
upper = 10000
integral =[]

for n in range (lower, upper):
    P= [0] +sorted([u(0,2) for i in range(n)])+[2]
    S=0
    for j in range(1, len(P)):
        w=P[j]-P[j-1]
        h=f(u(P[j-1], P[j]))
        S += w*h
    integral.append(S)
    
plt.plot(list (range(lower+1, upper+1 )), integral)   
plt.show