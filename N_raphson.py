import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
eqn=input("enter the equation in x using python syntax:")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)
def g(f,x,h=1e-10):
     return ((f(x+h)-f(x-h))/(2*h))
a = float(input('Enter the  initial guess :'))

if g(f,a)==0:
    print('Division by zero,change initial guesses')
else:
      e = float(input('Enter the tolerable error:'))
      N = int (input('Enter the max no of iterations:'))
      itr = 1
      A=[]
      M=[]
while itr<=N:
         b=a-(f(a)/g(f,a))
         A.append([itr,a,b,f(a),f(b)])
         M.append(b)
         err=abs(f(b))
         if err<e:
              A=pd.DataFrame(A,columns=['iterations','a','b','f(a)','f(b)'])
              print(A.to_string(index=False))
              print(f'Approx root is {b} in {itr} iterations') 
              break
         a=b
         if g(f,a)==0:
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
plt.title('Newton Raphson')
plt.legend()
plt.scatter(M,f(M))
for i,val in enumerate(M):
    plt.text(val,f(val),f'{i+1}')
    
plt.show()
