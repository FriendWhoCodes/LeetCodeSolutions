# https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/


def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
  
# Driver code
a = print(factorial(5))
