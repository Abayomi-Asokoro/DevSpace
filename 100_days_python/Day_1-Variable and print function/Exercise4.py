# Exercise 4
# Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.

# Tip: Use compound capitalization of interest.

# Print the result to the console as shown below.
# Expected result: The future value of the investment: 1159.27 USD
# 
import math

P = 1000 # Principal 
r = 0.03 # rate: 3%
t = 5 # time: 5yrs
I = P* (1 + r) ** t # Interest 

print(f"The future value of the investment: {round(I,2)} USD")
print(f"The future value of the investment: {I:.2f} USD")
