# Initialize a variable to store the total sum
total = 0

# Loop through numbers from 1 to 999
for number in range(1, 1000):
    # Check if the number is a multiple of 3 or 5
    if number % 3 == 0 or number % 5 == 0:
        # Add it to the total sum
        total += number

# Print the result
print("The sum of all multiples of 3 or 5 under 1000 is:", total)