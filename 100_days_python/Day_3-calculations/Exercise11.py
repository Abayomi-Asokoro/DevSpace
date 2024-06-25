# Exercise 3
# Find the roots of the quadratic equation:
# x^2 - 5x + 4 = 0
# (-b ± √ (b2 - 4ac) )/2a

# Print the result to the console as shown below.

# Expected result:
# x1 = -4.0
# x2 = -1.0

import math

a = 1
b = 5
c = 4

x2 = (-b + ((b**2 - 4*a*c))**(1/2) )/2*a
x1 = (-b - ((b**2 - 4*a*c))**(1/2) )/2*a

delta_sqrt = ((b**2 - 4*a*c))**(1/2)

print(f"x1 = {x1}")
print(f"x2 = {x2}")
