# create a game about rock paper scissors. Player have to write their choice and the computer will choose randomly. If player write something wrong, the game have to say it. 
# If player win, the game will say it. If player lose, the game will say it. If player and computer choose the same, the game will say it.

import random

print("="*15)
print('Welcome to Rock, Paper, Scissors game. You will play against the computer. Choose your weapon wisely!')
print("="*15)

continue_game = True

def game(player, computer):
    if (player == computer):
        print('It is a tie!')
    elif(player == 'rock' and computer == 'scissors'):
        print('You win!')
    elif(player == 'scissors' and computer == 'paper'):
        print('You win!')
    elif(player == 'paper' and computer == 'rock'):
        print('You win!')
    else:
        print('You lose!')

while continue_game:
  
    player = input('Choose your weapon: ')
    player = player.lower()
    
    while player not in ['rock', 'paper', 'scissors']:
        print('You choose wrong weapon. Please choose again!')
        player = input('Choose your weapon: ')
        player = player.lower()

    print("="*15)
    computer = random.choice(['rock', 'paper', 'scissors'])
    print('Computer choose: ' + computer)

    print("="*15)
    game(player, computer)
    print("="*15)
    
    print('Do you want to play again?')
    answer = input('Yes or No: ')
    answer = answer.lower()
    
    while answer not in ['yes', 'no']:
        print('Please choose Yes or No!')
        answer = input('Yes or No: ')
        answer = answer.lower()
    
    if(answer == 'no'):
        continue_game = False
    else:
        continue_game = True
    print("="*15)

print("="*15)
print('Thank you for playing!')