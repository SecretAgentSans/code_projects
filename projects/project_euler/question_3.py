num = 600851475143
current = num -1

def IsPrime(numToCheck):
    isPrime = False
    if numToCheck > 1:
        # check for factors
        for i in range(2, numToCheck):
            if (numToCheck % i) == 0:
                # if factor is found, set flag to True
                isPrime = False
                # break out of loop
                break
    return IsPrime

while True:
    if num % current == 0:
        if IsPrime(current):
            break
    current -= 1

print("largest prime number is",  current)