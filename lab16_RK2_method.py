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
x_val=[]
y_val=[]


for i in range(n):
    y_predict = y+h*f(x,y)
    y_correct = y+(h/2)* (f(x,y)+ f(x+h, y_predict))
    y=y_correct
    x=x+h
    t.append([x,y])
    x_val.append(x)
    y_val.append(y)
t=pd.DataFrame(t,columns=['x', 'y'])
print("Solutions: ")
print(t)
plt.plot(x_val, y_val, label = 'RK2 Method') 
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0,0, color='black')
plt.axvline(0,0, color='blue')
plt.legend()
plt.grid(True)
plt.title('RK2 Method:')
plt.show()