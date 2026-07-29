# Recursive Factorial

def factorial(n):
 if n == 0 or n == 1:
  return 1
 else:
  return n * factorial(n-1)
print("Factorial of 8:", factorial(8))  