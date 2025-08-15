import numpy as np
import matplotlib.pyplot as plt

a = float(input('Enter the lower limit of integration: '))
b = float(input('Enter the upper limit of integration: '))
n = int(input('Enter the number of sub-interval: '))
h = (b - a) / n

func = input('Enter the integrand function in python: ')
def f(x):
    return eval(func)

x_values = np.linspace(a, b, n+1)
y_values = [f(x) for x in x_values]

sum_3 = 0   # for indices not divisible by 3
sum_2 = 0   # for indices divisible by 3 (excluding 0 and n)

for i in range(1, n):
    if i % 3 == 0:
        sum_2 += y_values[i]
    else:
        sum_3 += y_values[i]

integral = (3 * h / 8) * (y_values[0] + 3 * sum_3 + 2 * sum_2 + y_values[n])
print(f"The approximate integral value is {integral}")

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, color='blue', label='f(x)')

x_fine = np.linspace(a, b, 1000)
y_fine = [f(x) for x in x_fine]
plt.plot(x_fine, y_fine, linestyle='--', color='black')

for i in range(0, n, 3):
    xs = x_values[i:i+4]
    ys = y_values[i:i+4]
    if len(xs) == 4:
        plt.fill(xs, ys, facecolor='orange', edgecolor='green', alpha=0.3)

plt.title("Simpson's 3/8 Rule Approximation")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()