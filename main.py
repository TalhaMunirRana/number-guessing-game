import random

print("--- Number Guessing Game ---")

number = random.randint(1, 10)


print("I picked a number between 1 and 10")

while True:
    guess = int(input("Your Guess: "))

    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Correct")
        play_again = input("Do you want to play again? (Yes/No) ")

        if play_again.lower() == 'yes':
            continue
        elif play_again.lower() == 'no':
            break