import numpy as np
import matplotlib.pyplot as plt 

# Input from user
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of partitions (must be even): "))

if n % 2 != 0:
    raise ValueError("Number of partitions must be even for Simpson's 1/3 rule.")

h = (b - a) / n
func = input("Enter the integrand function in x using python syntax (e.g., x**2 + 3*x): ")

def y(x):
    return eval(func)

x = np.linspace(a, b, n + 1)
S1 = 0
S2 = 0

for i in range(1, n):
    if i % 2 != 0:
        S1 += y(x[i])
    else:
        S2 += y(x[i])

I = (h / 3) * (y(x[0]) + 4 * S1 + 2 * S2 + y(x[n]))

# Output result
print(f"The approximate integral by Simpson's 1/3 rule is {I:.6f}")

# Plotting
y_points = [y(val) for val in x]
plt.plot(x, y_points, color='red', label="Simpson Approximation")
xval = np.linspace(a - 1, b + 1, 1000)
plt.plot(xval, [y(val) for val in xval], label='Function Curve')

plt.axvline(0, color='black', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)

# Simpson's segment shading
for i in range(0, n-1, 2):
    xs = x[i:i+3]
    ys = y_points[i:i+3]
    if len(xs) == 3:
        plt.fill_between(xs, ys, color='red', edgecolor='black', alpha=0.5)

plt.legend()
plt.title("Integration using Simpson's 1/3 Rule")
plt.grid(True)
plt.show()
