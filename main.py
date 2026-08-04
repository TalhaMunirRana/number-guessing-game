import random

print("--- Number Guessing Game ---")

# Generate a Random number
number = random.randint(1, 10)
print("I picked a number between 1 and 10")

# Attempt counter
attempts = 0

while True:
    guess = int(input("Your Guess: "))
    attempts += 1 # Increment 1 in attempts

    if guess > number:
        print("Too High!")
        
    elif guess < number:
        print("Too Low!")
    else:
        print("Congratulations! You guessed the number " + str(number) + ".")
        print("You won in " + str(attempts) + " attempts.")
        break