import random

secret_number=random.randint(1, 10)

while True:
    guess=input("Guess a number between 1 and 10: ")
    guess=int(guess)

    if guess==secret_number:
       print('🎉 Congratulations! You guessed it right.')
       break
    elif guess < secret_number:
        print('Too low! Try again.')
    else:
        print('Too high! Try again.')
