#!/usr/bin/python3
# List Prime Numbers

# Work Out If A Provided Number Is A Prime Number
def is_prime_number(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


### Main Section

# Ask User For Upper Limit Of List
limit=int(input("Upper Limit: "))+1

# Loop Numbers And Build List
print('2');
for x in range(3,limit):
    if not x % 2 == 0:
        if is_prime_number(x):
            print (x)

