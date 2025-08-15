#to solve the system of linear equation by gauss seidal by using python
import numpy as np
import pandas as pd

# Input number of variables
n = int(input("Enter the number of variables: "))
A = []


# Input augmented matrix
print("Enter the augmented matrix (each row should include the RHS as the last value):")
for i in range(n):
    A.append(list(map(float, input(f'Enter row {i+1}: ').split())))

A = np.array(A)
print("The augmented matrix is:")
print(A)

# Initial guess
x = np.array(list(map(float, input("Enter initial guess vector: ").split())))
print("Initial guess:")
print(x)

# Error tolerance and number of iterations
e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

# Gauss-Seidel iteration
itr = 1
T=[]
while itr <= N:
    x_old = np.copy(x)
    
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i, j] * x[j]
        x[i] = (A[i, -1] - s) / A[i, i]
    
    T.append([itr]+ [x[i] for i in range(n)])
    error = abs(x - x_old)
    if np.all(error < e):
        break
    itr += 1

if itr > N:
    print("Solution does not converge!")
else:
    T= pd.DataFrame(T,columns=["iteration "]+ [f'x{i+1}' for i in range(n)]).to_string(index=False)
    print(T)
    print("The solution is:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")



