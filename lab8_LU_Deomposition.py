#to solve the system of linear equattion by lu decomposition method

#import
import scipy.linalg as slg
import numpy as np

#input
n= int(input("Enter the no of variables:"))
A=[]


for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row:").split())))

A= np.array(A)
print("The coeff matrix in A: \n",np.matrix(A))

B = np.array(list(map(float,input("Enter the output vector:").split())))
B = np.array(B)
print("The output matrix of B: \n ",np.matrix(B))

P,L,U = slg.lu(A)
lum = slg.lu_factor(A)

print("The lower triangular matrix is L:\n",L)
print("The upper triangular matrix is L:\n",U)
print("THe permutation matrix is P:\n",P)
x= slg.lu_solve(lum,B)
print("THe solution is:\n",x)
