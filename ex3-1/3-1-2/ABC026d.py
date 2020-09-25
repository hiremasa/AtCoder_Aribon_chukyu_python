import numpy as np
from scipy import optimize
A, B, C = map(int, input().split())
def f(x): return A*x + B*np.sin(C*x*np.pi)-100
print(optimize.newton(f, 0))