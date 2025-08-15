import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode= input("Enter dy/dx interms of x and y using python syntax: ")

def F(x,y, ode):
    return eval(ode)
def f(x,y):
    return F(x,y,ode)
x=float(input("Enter initial value of x: "))
y= float(input("Enter value of y: "))
h=float(input("Enter step-size value: "))
n= int(input("Enter the number of steps: "))
t=[]
x_list=[]
y_list=[]


for i in range(n):
    k1= h*f(x,y)
    k2= h*f(x+h/2, y+k1/2)
    k3= h*f(x+h/2, y+k2/2)
    k4= h*f(x+h, y+k3)
    y= y+(1/6)*(k1+2*k2+ 2*k3+ k4)
    x=x+h
    t.append([x,y])
    x_list.append(x)
    y_list.append(y)
t=pd.DataFrame(t,columns=['x', 'y'])
print("Solutions: ")
print(t)
plt.plot(x_list,y_list,color='blue',label='RK4 method') 
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0,0, color='black')
plt.axvline(0,0, color='blue')
plt.legend()
plt.grid(True)
plt.title('R_K_4 METHOD.')
plt.show()