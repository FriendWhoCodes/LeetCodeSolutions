# https://www.geeksforgeeks.org/python-program-for-compound-interest/

# Calculating compund interest annually
# Formula is:
# C = A - P
# and A = P*(1 + R)^t

def compound_interest(principal_amount, rate, time):
    yearly_amount = principal_amount * (1 + rate / 100) ** time
    comp_interest = yearly_amount - principal_amount
    return comp_interest

# Driver program
print(compound_interest(1000, 2, 2))
