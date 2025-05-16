import random  # Importing the module to generate random numbers

print("Welcome to the Number Guessing Game!") 
print("I'm thinking of a number between 1 and 100...")

# The computer randomly chooses a number between 1 and 100
secret_number = random.randint(1, 100)

# Start the game loop
attempts = 0  # We use this to count how many guesses the user makes

while True:
    # Ask the user to guess the number
    guess = input("Enter your guess: ")

    # Check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue  # Skip the rest of the loop and ask again

    guess = int(guess)  # Convert the input string to an integer
    attempts += 1  # Count this as a guess attempt

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # Correct guess!
        print(f"Congratulations! You guessed the number in {attempts} tries.")
        break  # Exit the loop
