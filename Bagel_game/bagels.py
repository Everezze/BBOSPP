import random

def main():

    PLAYER_GUESSES =1
    TRIES_ALLOWED=10
    NUM_DIGITS=3

    RANDOM_NUMBER= random_num(NUM_DIGITS)


    while PLAYER_GUESSES <= TRIES_ALLOWED:

        HINTS=[]
        GUESS = get_guess(NUM_DIGITS,PLAYER_GUESSES)

        if RANDOM_NUMBER == GUESS:
            print(f'Congratulations! You won in {PLAYER_GUESSES} tries')
            return 1 

        for index in range(NUM_DIGITS):
            if RANDOM_NUMBER[index] == GUESS[index]:
                HINTS.append('Fermi')
            elif GUESS[index] in RANDOM_NUMBER:
                HINTS.append('Pico')

        if len(HINTS) ==0:
                HINTS.append('Bagles')

        print(*HINTS)
        PLAYER_GUESSES +=1

    print(f'You tried your best but your {TRIES_ALLOWED} tries are exhausted, the answer was {RANDOM_NUMBER}')


def random_num(NUM_DIGITS):
    rand_num= ''
    numbers= '0123456789'

    while len(rand_num) < NUM_DIGITS:
        x= numbers[random.randint(0,9)]
        if x not in rand_num:
            rand_num += x

    return rand_num

def get_guess(NUM_DIGITS,PLAYER_GUESSES):

    while True:
        print(f"Guess #{PLAYER_GUESSES}")
        valid_guess = input("> ")
        if valid_guess.isdecimal() and len(valid_guess) == NUM_DIGITS:
            return valid_guess
        else:
            print("Please insert a 3 digit valid number")




print('''Welcome to the bagels game, a deduction game.
I\' m thinking of a 3 digit number with no repeated digits.
Try to guess it, you have 10 tries to succeed
Here\'s the meaning of the hints:

 -------------------------------------
|  Hint  |           Meaning          |
 -------------------------------------
| Picko  | correct digit, wrong place |
 -------------------------------------
| Fermi  | correct digit, right place |
 -------------------------------------
| Bagels |      no correct digits     |
 ------------------------------------- 

 ''')

while True:
    main()
    replay= input('Do you want to play again?[yes/y or N/n] : ')
    if replay.lower() == "yes" or replay.lower() == "y":
        continue
    else:
        print("Thanks for playing")
        break
