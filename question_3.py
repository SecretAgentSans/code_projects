import math

num = 600851475143
current = 2
largest = 0

def IsPrime(numToCheck):
    if numToCheck <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(numToCheck)) + 1):
            if numToCheck % i == 0:
                return False
    return True

while current <= num:
    if num % current == 0:
        if IsPrime(current):
            largest = current
            num //= current
            continue
    current += 1

print("largest prime number is",  largest)