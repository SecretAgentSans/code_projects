total = 0
previous = 0
current = 1

while current < 4000000:
    temporary = previous + current
    if temporary % 2 == 0:
        total += temporary
    previous = current
    current = temporary

print("fibbonachi things:", total)