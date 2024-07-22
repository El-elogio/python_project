from random import shuffle

tiger = [' ', 'O', ' ']


def shuffle_list(tee):
    shuffle(tee)
    return tee


hi = shuffle_list(tiger)


def player_guess():
    guess = ' '
    while guess not in ['0', '1', '2']:
        guess = input('Make a guess from either 0, 1 or 2: ')
    return int(guess)


gu = player_guess()


def check_guess():
    if hi[gu] == 'O':
        print('correct')

    else:
        print('wrong')
    print(tiger)


check_guess()


# play a guessing game with my bot
secret_number = 21
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('WHATS YOUR GUESS: '))
    guess_count += 1
    if guess == secret_number:
        print("SMART ASS")
        break

else:
    print("OUCH, TRY AGAIN!!!")