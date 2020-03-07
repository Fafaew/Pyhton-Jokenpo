from random import randint
from time import sleep
choices = ('Rock', 'Paper', 'Scisors')
computer = randint(0, 2)
print('''Options
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISORS''')
player = int(input('Whats your choice? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 15)
print('Computer choice: {}'.format(choices[computer]))
print('Player choice: {}'.format(choices[player]))
print('-=' * 15)

if computer == 0:  
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('Player Wins!')
    elif player == 2:
        print('Computer win')
    else:
        print('Invalid Choice')
elif computer == 1: 
    if player == 0:
        print('Computer win')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('Players Wins!')
    else:
        print('Invalid Choice')
elif computer == 2:  
    if player == 0:
        print(' Player Wins!')
    elif player == 1:
        print('Computer win')
    elif player == 2:
        print('DRAW')
    else:
        print('Invalid choice')