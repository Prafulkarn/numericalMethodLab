import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

eqn = input('enter the eqn in x using Python syntax:')

def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)

a = float(input('Enter the first initial value :'))
b = float(input('Enter the second initial value :'))

if f(a) * f(b) > 0:
    print("The function has the same sign at the endpoints a and b. Please choose different values.")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the maximum number of iterations: "))
    itr = 1
    itr_table = []

    while itr <= N:
        # Regula Falsi formula
        c = (a*f(b) - b*f(a))/(f(b) - f(a))

        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        # Update the bracket
        if fa * fc < 0:
            b = c
        else:
            a = c

        er = abs(fc)  # Error estimate using function value

        itr_table.append([itr, a, b, c, fa, fb, fc, er])

        if abs(fc) < e:
            itr_table = pd.DataFrame(itr_table, columns=['Itr', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'er'])
            print(itr_table.to_string(index=False))
            print(f"\nApproximate root is: {c} in {itr} iterations")
            break


        itr += 1

    if itr > N:
        print(f"\nThe solution did not converge within {N} iterations.")
    else:
        print("\nEnd")

# Plotting the function
x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), label=eqn, color='red')
plt.axhline(0, color='blue', linestyle='--')
plt.axvline(0, color='green', linestyle='--')
plt.title('Regula Falsi Method Function Plot')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
