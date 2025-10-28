import random

#Defining variables
random_number = random.randint(1, 100)
guess_count = 0
max = 10

print("Welcome to the Number Guessing Game!")
print(f"Can you find the secret number between 1 and 100 in {max} tries?")

#This loop checks the guess_count and ValueError 
while guess_count < max:
    guesses_left = max - guess_count
    guess_string = input(f"Make a guess, {guesses_left} guesses left: ")

    try:
        guess = int(guess_string)
        guess_count += 1
    
    except ValueError:
        print("This doesn't look like a valid number! Please make another guees")
        print("Don't worry this won't be counted as a guess")
        continue

#This if/else part gives player feedback (clues or win message)
    if guess < random_number:
        print("To low, increase your guess!")
    elif guess > random_number:
        print("To high, decrease your guess!")
    else:
        print("Congratulations!")
        print(f"You guessed the number, it was {random_number}.")
        print(f"You guessed it in {guess_count} tries")
        break #Exit the loop (You win)

#This else block runs only if the player runs out of guesses
else:
    print("Sorry you are out of guess")
    print(f"Secret number was {random_number} ")



