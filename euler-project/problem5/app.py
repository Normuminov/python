"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num = 20

while num < 3000000000:
    for i in range(20, 0, -1):
        if num % i != 0:
            num += 1
            break
            
        if i == 1:
            print(num)

# The actual answer is too large (232,792,560). It will take ages for a normal pc to compute!