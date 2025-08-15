import scipy.linalg as slg
import numpy as np
import pandas as pd

#input
n= int(input("Enter the order of matrix:"))
A=[]


for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row:").split())))

A= np.array(A)
print("The square matrix in A: \n",np.matrix(A))

X = np.array(list(map(float,input("Enter the initial vector:").split())))
X = np.array(X)
print("The initial matrix of X: \n ",np.matrix(X))

# Error tolerance and number of iterations
e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

itr=1
old_eigen_value=0
T=[]

while itr<=N:
    Y= np.dot(A,X)
    max_eigen_value= abs(max(Y,key=abs))
    for i in range(n):
        X=Y/max_eigen_value
    
    T.append([itr,max_eigen_value]+ [X[i] for i in range(n)])
    error= abs(max_eigen_value-old_eigen_value)
    if error<e:
        break

    old_eigen_value= max_eigen_value
    itr +=1

if itr>N:
    print(f"No dominant eigen value is found in {N} iteration")

else:
    T= pd.DataFrame(T,columns=["iteration ","Max eigenvalue"]+ [f'X{i+1}' for i in range(n)]).to_string(index=False)
    print(T)
    print(f'The dominant eigen value is {max_eigen_value} in {itr} iterations')
    print('The corresponding eigen vector is x:\n',np.matrix(X))