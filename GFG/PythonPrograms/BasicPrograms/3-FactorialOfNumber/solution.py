# https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/

# Recursive

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
  
  
# Driver code
a = print(factorial(5))

# Iterative


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        factorial = n
        while n > 1:
            factorial = factorial * (n -1)
            n -= 1
    return factorial
  
# Driver code
a = print(factorial(6))
