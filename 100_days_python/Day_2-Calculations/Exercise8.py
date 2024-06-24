# Exercise 3
# The geometric sequence is given with the following formula:
# S(n) = 8 . 2^n-1 : nth-term

# Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.

# Expected result: The sum of the first 6 elements of the sequence is: 504.0

n = 6
a = 8
r = 2

sum1 = a*(1 - r**n) / (1 - r)

print(f"The sum of the first 6 elements of the sequence is: {sum1}")
