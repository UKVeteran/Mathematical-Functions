from math import cos, sin, pi
import matplotlib.pyplot as plt

T= [2*pi /1000000*x for x in range(1000000)]
X=[2*cos(t)+7*cos(t)**2 for t in T]
Y= [2*sin(t) + 7*cos(t)*sin(t) for t in T]


plt.plot(X,Y)
plt.show()