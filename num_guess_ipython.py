import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and %s: ' % x))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print('Yay, congrats. You have guessed the number %s correctly!!' % random_number)

def computer_guess(x):
    print(f'Choose a number between 1 and {x} for the computer to guess.')
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input('Is %s too high (H), too low (L), or correct (C)?? ' % guess).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay! The computer guessed your number, %s, correctly!' % guess)


guess(10)
computer_guess(19)
