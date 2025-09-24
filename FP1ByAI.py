import random
import time

# --- Helper class for terminal colors ---
class colors:
    """A class to hold ANSI escape codes for terminal colors."""
    RED = '\033[91m'    # The code for red text
    RESET = '\033[0m'   # The code to reset to default color

# Greet the user and ask for their name
print("Welcome to the Lucky Number Generator! 🍀")
varUserName = input("What is your name? ")

# Greet the user personally using their name
print(f"\nHello, {varUserName}! Here are your lucky numbers:")

# Generate six random integers and store them in a list
lucky_numbers = [random.randint(1, 50) for _ in range(6)]

# Loop through the first five numbers to print them with a delay
for i in range(5):
    # Pause the program for 0.25 seconds
    time.sleep(0.25)

    # Determine the spacing based on the number's position
    spacing = "    " if i == 4 else "  "

    # Print the number, but use 'end=spacing' to prevent a new line
    # and add our custom spacing. 'flush=True' ensures it prints immediately.
    print(lucky_numbers[i], end=spacing, flush=True)

# Pause one last time before the final number
time.sleep(0.25)

# Print the final number in RED, then reset the color
final_number = lucky_numbers[5]
print(f"{colors.RED}{final_number}{colors.RESET}")


# Display a farewell message
print(f"\nGood luck, {varUserName}! Have a great day.")