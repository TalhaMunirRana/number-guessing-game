import random

def choose_difficulty():
    """Returns the upper limit according to the difficulty."""
    while True:
        difficulty = input("\nChoose difficulty: \n1. Easy (1 -10)\n2. Medium (1 -50)\n3. Hard (1 -100)\n")
        if difficulty == '1':
            return 10
        elif difficulty == '2':
            return 50
        elif difficulty == '3':
            return 100
        else:
            print("Invalid Input!")
            continue

def generate_secret_number(upper_limit):
    """Returns a generated random number based on upper limit."""
    secret_number = random.randint(1, upper_limit)
    print(f"I picked a number between 1 and {upper_limit}.")
    return secret_number

def play_game(secret_number):
    """Contains the game logic."""
    # Attempt counter
    attempts = 0

    while True:
        guess = int(input("Your Guess: "))
        attempts += 1
    
        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        else:
            print(f"Congratulations! You guessed the number {secret_number}.")
            print(f"You won in {attempts} attempts.")
            break

def play_again():
    """Asks the user if they want to play again or not."""
    again = input("Play again? (y/n) ")
    return again.lower() != 'n'

print("--- Number Guessing Game ---")

# Start the game loop
while True:
    # Choose difficulty level
    upper_limit = choose_difficulty()

    # Generate the random number
    secret_number = generate_secret_number(upper_limit)

    play_game(secret_number)

    if not play_again():
        break
    