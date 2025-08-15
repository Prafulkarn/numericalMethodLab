# import
import scipy.linalg as slg
import numpy as np
import pandas as pd

# input
n = int(input("Enter the order of matrix: "))
A = []

for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row: ").split())))

A = np.array(A)
print("The square matrix A: \n", np.matrix(A))

def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print("Matrix is singular")
        exit()

inv_A = inv(A)
print("The inverse of A:\n", np.matrix(inv_A))

X = np.array(list(map(float, input("Enter the initial vector: ").split())))
print("The initial vector X: \n", np.matrix(X).T)

# Error tolerance and number of iterations
e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

itr = 1
old_eigen_value = 0
T = []

while itr <= N:
    Y = np.dot(inv_A, X)
    max_eigen_value = max(abs(Y))
    X = Y / max_eigen_value

    least_eigen_value = 1 / max_eigen_value
    T.append([itr, least_eigen_value] + [X[i] for i in range(n)])

    error = abs(max_eigen_value - old_eigen_value)
    if error < e:
        break

    old_eigen_value = max_eigen_value
    itr += 1

if itr > N:
    print(f"No least eigen value is found in {N} iterations")
else:
    T = pd.DataFrame(T, columns=["Iteration", "Least Eigenvalue"] + [f'X{i+1}' for i in range(n)]).to_string(index=False)
    print(T)

    print(f"\nThe least eigen value is {least_eigen_value} found in {itr} iterations")
    print('The corresponding eigen vector is:\n', np.matrix(X).T)
