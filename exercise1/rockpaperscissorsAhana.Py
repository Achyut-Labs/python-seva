'''
Rock Paper Scissors
-------------------------------------------------------------
'''


import random
import os
import re


def check_play_status():
  valid_responses = ['yes', 'no']
  while True:
      try:
          response = input('Do you wish to play again? (Yes or No): ')
          if response.lower() not in valid_responses:
              raise ValueError('Yes or No only')\
              

          if response.lower() == 'yes':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():
   play = True
   while play:
    
       print('')
       print('Rock, Paper, Scissors - Shoot!')

       user_choice = input('Choose your weapon'
                           ' [Rock]rock], [Paper]paper, or [Scissors]scissors: ')

       if not re.match("[ScissorsRockPaper]", user_choice):
           print('Please choose a word:')
           print('[Rock]rock, [Paper]paper, or [Scissors]scissors')
           continue

       print(f'You chose: {user_choice}')

       choices = ['Rock', 'Paper', 'Scissors']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice}')

       if opp_choice == user_choice.upper():
           print('Tie!')
           play = check_play_status()
       elif opp_choice == 'Rock' and user_choice.upper() == 'Scissors':
           print('Rock beats scissors, I win!')
           play = check_play_status()
       elif opp_choice == 'Scissors' and user_choice.upper() == 'Paper':
           print('Scissors beats paper! I win!')
           play = check_play_status()
       elif opp_choice == 'Paper' and user_choice.upper() == 'Rock':
           print('Paper beats rock, I win!')
           play = check_play_status()
       else:
           print('You win!\n')
           play = check_play_status()


if __name__ == '__main__':
   play_rps()
