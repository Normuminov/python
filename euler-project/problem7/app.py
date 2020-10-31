"""
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10,001st prime number?
"""

prime = 0
num = 2

while prime < 10002:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime += 1
    
    num += 1

print(num)

# Ouptut: 