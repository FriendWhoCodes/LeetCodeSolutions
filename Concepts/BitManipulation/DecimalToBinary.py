# Convert a decimal to binary number and also count total number of bits


stack = []
n = 100
rem = 0
print("Decimal number is: ", n)
print("Binary number is: ", bin(n))

while n > 0:
    rem = n % 2
    stack.append(rem)
    n >>= 1
# Since the binary number is the reverse of remainders, so reverse it
stack.reverse()
binary = ''.join(map(str, stack))
print("Converted decimal to binary is: ", binary)
print("Number of bits in the number are: ", len(stack))


'''
# Sample Output:

Finished in 36 ms
Decimal number is:  1024
Binary number is:  0b10000000000
Converted decimal to binary is:  10000000000
Number of bits in the number are:  11

Finished in 51 ms
Decimal number is:  10
Binary number is:  0b1010
Converted decimal to binary is:  1010
Number of bits in the number are:  4

Finished in 47 ms
Decimal number is:  100
Binary number is:  0b1100100
Converted decimal to binary is:  1100100
Number of bits in the number are:  7

'''
