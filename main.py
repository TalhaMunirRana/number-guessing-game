import random

print("--- Number Guessing Game ---")

# Start the game loop
while True:
    # Choose difficulty level
    difficulty = input("\nChoose difficulty: \n1. Easy (1 -10)\n2. Medium (1 -50)\n3. Hard (1 -100)\n")
    if difficulty == '1':
        upper_limit = 10
    elif difficulty == '2':
        upper_limit = 50
    elif difficulty == '3':
        upper_limit = 100
    else:
        print("Invalid Input!")
        continue

    # Generate the random number
    secret_number = random.randint(1, upper_limit)
    print(f"I picked a number between 1 and {upper_limit}.")

    # Attempt counter
    attempts = 0

    while True:
        guess = int(input("Your Guess: "))
        attempts += 1 # Increment 1 in attempts

        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        else:
            print(f"Congratulations! You guessed the number {secret_number}.")
            print(f"You won in {attempts} attempts.")
            break

    again = input("Play again? (y/n) ")

    if again.lower() == 'y':
        continue
    else:
        break