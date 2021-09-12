from sympy.solvers import solve
from sympy import *
x=Symbol('x')

solutions=solve(x**3 +x-132, x , dict=True)
for i in solutions:
    print(i.get(x))