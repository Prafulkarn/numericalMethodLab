#To evaluate integration: a -> b f(x) dx by using simpson's 1/3 rule


import numpy as np
import matplotlib.pyplot as plt 
# to evaluate integration [a to b] f(x) dx using simpson rule 
a=float(input("Enter the lower limit of integration: "))
b=float(input("Enter the upper limit of integration "))
n=int(input("Enter the number of partitions "))
h=(b-a)/n
func=input("Enter the integrand function in x using python syntax: ")
def f(x,func):
    return eval(func)
def y(x):
    return f(x,func)
x=np.linspace(a,b,n+1)
I=0
S1=0
S2=0
for i in range(1,n):
    if i%2!=0:
        print('Number of partition is not even')
        exit()
    
        
    else:
        S1+=y(x[i])
        S2+=y(x[i])
I=(h/3)*(y(x[0])+4*S1+2*S2+y(x[n]))
y_points=[y(x) for x in x]
print(f"The appriximate integral by simpson rule is {I}")
plt.plot(x,y_points,color='red',label="graph")
xval=np.linspace(a-1,b+1,1000)
plt.plot(xval,[y(x) for x in xval],label='eqn of curve')
plt.axvline(0,0)
plt.axhline(0,0)
for i in range(0,n,2):
    xs=x[i:i+3]
    ys=y_points[i:i+3]
    plt.fill_between(xs,ys,color='red',edgecolor='black',alpha=0.5)
plt.show()