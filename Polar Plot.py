from math import cos,  sin, pi
import matplotlib.pyplot as plt

def f(t): return 4*sin(2*t) + 2*cos(3*t)-3*cos(4*t) -4*sin(3*t)

n=50000
T=[2*pi/n*x for x in range(n)]
X1=[cos(t)*f(t)**.5  for t in T if f(t)>=0]
Y1=[sin(t)*f(t)**.5  for t in T if f(t)>=0]
X2=[-x for x in X1]
Y2=[-y for y in Y1]

plt.plot(X1+X2,Y1+Y2)
plt.show()