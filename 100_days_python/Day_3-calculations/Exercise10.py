# Exercise 2
# Calculate the distance of two points A = (3, 2), B = (- 1, -1) and print result to the console as shown below.


# Expected result: The distance between points A and B: 5.0
import math

x1,x2= 3, 2
y1,y2= -1, -1

Mx = (x2 - x1)**2
My = (y2 - y1)**2

MPxy = math.sqrt(Mx + My)

print(f"The middle point: {MPxy}")


Mxyi = (x1 - y1)**2
Mxyii = (x2 - y2)**2

MPxy = math.sqrt(Mxyi + Mxyii)
MPxy = (Mxyi + Mxyii)**(1/2)

print(f"The distance between points A and B: {MPxy}")
