"""
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check(num):
    for k in range(len(num)//2):
        if num[k] != num[-k - 1]:
            return False
    return True

num = 0
arr = []

for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        num = i * j

        if check(str(num)):
            arr.append(num)

print(max(arr))

# Output: 906609