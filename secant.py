import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
eqn=input("enter the equation in x using python syntax")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)
a = float(input('Enter the first initial value :'))
b = float(input('Enter the second initial value :'))
if f(a)==f(b):
    print('Division by zero,change initial guesses')
else:
     e = float(input('Enter the tolerable error:'))
     N = int (input('Enter the max no of iterations:'))
     itr = 1
     A=[]
     M=[]
while itr<=N:
         c=(a*f(b)-b*f(a))/(f(b)-f(a))
         A.append([itr,a,b,c,f(a),f(b),f(c)])
         M.append(c)
         err=abs(f(c))
         if err<e:
              A=pd.DataFrame(A,columns=['iterations','a','b','c','f(a)','f(b)','f(c)'])
              print(A.to_string(index=False))
              print(f'Approx root is {c} in {itr} iterations') 
              break
         a,b=b,c
         if f(a)==f(b):
              print('Divison by zero,change initial guesses')
              break
         itr+=1
         if itr>N:
              print(f"solution doesn't converge in {N} iteration")

M = np.array(M)
x = np.linspace(-5,5,1000)
plt.plot(x,f(x),color='red', label=eqn)
plt.axhline(0,0,color='blue')
plt.axvline(0,0,color='black')
plt.grid(True)
plt.xlabel("x")
plt.ylabel('f(x)')
plt.title('Secant method')
plt.legend()
plt.scatter(M,f(M))
for i,val in enumerate(M):
    plt.text(val,f(val),f'{i+1}')
    
plt.show()
