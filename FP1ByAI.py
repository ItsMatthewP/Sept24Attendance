# Import the random module to generate random numbers
import random

# Greet the user and ask for their name
print("Hello! Welcome to the Lucky Number Generator.")
varUserName = input("What is your name? ")

# Greet the user personally and introduce the numbers
print(f"\nIt's a pleasure to meet you, {varUserName}.")
print("Here are your six lucky numbers:")

# --- Generate and Format the Numbers ---

# 1. Generate a list of six random integers between 1 and 50
numbers = [random.randint(1, 50) for _ in range(6)]

# 2. Format the numbers for printing according to the instructions.
#    - '  '.join(map(str, numbers[:5])) takes the first five numbers, converts them to strings,
#      and joins them together with two spaces in between each.
#    - '    ' + str(numbers[5]) adds four spaces and then the final number.
output_string = '  '.join(map(str, numbers[:5])) + '    ' + str(numbers[5])

# 3. Print the final, formatted string of numbers
print(output_string)

# Display a farewell message
print(f"\nGood luck, {varUserName}!")