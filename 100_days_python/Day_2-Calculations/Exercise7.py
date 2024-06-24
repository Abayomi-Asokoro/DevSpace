# Exercise 2
# The arithmetic sequence is given with the following formula:
# a(n) = 10 + 4n : nth-term
# Sn = (n/2) [2a1 + (n - 1) d] (or) (n/2) [a1 + an]

# Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.

# Expected result:The sum of the first 10 elements in a sequence: 320.0



n = 10
a = 14
d = 4

sum1 = (n/2)*((2*a + (n-1)*d))

print(f"The sum of the first 10 elements in a sequence: {sum1}")

# n = a1 + (n - 1) d