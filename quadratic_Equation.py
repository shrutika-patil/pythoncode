# Q Python Program to Solve Quadratic Equation

#quadratic equation is ax**2 + bx + c 

# import complex math module

import cmath

a=1
b=5
c=6

e=(b**2) - (4*a*c)

sol1=(-b+cmath.sqrt(e))/(2*a)
sol2=(-b-cmath.sqrt(e))/(2*a)

print(f'The result of quadratic is {sol1} and {sol2}')
