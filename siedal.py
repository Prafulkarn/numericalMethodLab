import numpy as np
import pandas as pd

n=int(input('Enter the number of variables: '))
A=[]
for i in range(n):
    A.append(list(map(float,input(f'Enter {i+1}th row of augmented matrix:').split())))
A=np.array(A)
print("The augmented matrix is A: \n",np.matrix(A))
x=np.array(list(map(float,input('Enter the initial guess:').split())))
print('The initial guess is x:\n',np.matrix(x))
e = float(input("Enter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

itr = 1
T=[]
while itr <= N:
    x_old = np.copy(x)
    
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i, j] * x_old[j]
        x[i] = (A[i, -1] - s) / A[i, i]
    T.append([itr]+ [x[i] for i in range(n)])    
    error = abs(x - x_old)
    if np.all(error < e):
        break
    itr += 1
if itr > N:
    print("Solution does not converge in {N} iterations")
else:
    T=pd.DataFrame(T,columns=['Iterations']+[f'x{i+1}'for i in range(n)]).to_string(index=False)
    print(T)
    print("The solution is:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")
    
