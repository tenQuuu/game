import random

plr = input('choose your weapon: ')
com = random.randint (1, 3)
bool = True
while bool:
    if plr == 'rock':
        print('paper! you loose')
        break
    elif plr == 'paper':
        print('scissors! loooooooser :)')
        break
    elif plr == 'scissors':
        print('rock! haha')
        break
    else:
        print('play like a man...')
        break