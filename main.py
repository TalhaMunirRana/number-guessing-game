import random

print("--- Number Guessing Game ---")

# Choose difficulty level
difficulty = input("Choose difficulty: \n1. Easy (1 -10)\n2. Medium (1 -50)\n3. Hard (1 -100)\n")
if difficulty == '1':
    upper_limit = 10
elif difficulty == '2':
    upper_limit = 50
elif difficulty == '3':
    upper_limit = 100

# Generate the random number
number = random.randint(1, upper_limit)
print("I picked a number between 1 and " + str(upper_limit) + ".")

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