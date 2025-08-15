#to solve the system of linear equation by guss elimination with partial pivoting by using python 
import numpy as np
import pandas as pd


n = int(input("Enter the no of variables:"))
A=[]

print("Enter the augment matrix:")

for i in range(n):
    A.append(list(map(float, input(f'Enter {i+1}th row:').split())))

A= np.array(A)
print("The augmented matrix is A:")
print(np.matrix(A))

for i in range(n):
    p_row= np.argmax(np.abs(A[i:,i])) +i #goes to index wise positions in row
    A[[i,p_row]]=A[[p_row,i]]

    for j in range(i+1,n): #for second row
     
        A[j]=A[j]-A[j,i]/A[i,i]*A[i]

print('The upper triangular matrix is:')
print(np.matrix(A))
x=np.zeros(n)
for i in range(n-1,-1,-1):
    x[i]= (A[i,-1]- np.sum(A[i,i+1:n]*x[i+1:n]))/A[i,i]
print("The solution :")
for i in range(n):
    print(f"x{i+1}={x[i]:.3f}")
