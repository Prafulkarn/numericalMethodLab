#to evaluate integration: a -> b f(x) dx by using trapezordal Rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit of integration: '))
b = float(input('Enter the upper limit of integration: '))
n = int(input("Enter the number of partition: "))
h = (b - a)/n
func = input("Enter the integrand function in x using python syntax: ")
def f(x, func):
    return eval(func)

def y(x):
    return f(x, func)

x = np.linspace(a, b, n + 1)
I = 0
S = 0

for i in range(1 ,n):
    S += y(x[i])

I = (h/2)*(y(x[0]) + 2*S + y(x[i]))
yPoints = [y(x) for x in x]
plt.plot(x, yPoints, color = 'blue', label = 'TrapezordalRule')
xVal = np.linspace(a - 10, b + 10, 1000)
plt.plot(xVal, [y(x) for x in xVal], label='Equation of curve')
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, yPoints[i], yPoints[i+1], 0]
    plt.fill(xs, ys, color = 'red', edgecolor = 'black', alpha = 0.2)
plt.xlabel("Values")
plt.ylabel("y values")
plt.legend()
plt.grid(True)
plt.show()



print(f"The approximate integral by Trapezoidal Rule is: {I}")


