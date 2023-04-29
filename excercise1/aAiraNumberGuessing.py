'''
Number Guessing Game
-------------------------------------------------------------
'''

import random

attempts_list = []


def show_score():
  if not attempts_list:
      print('There is currently no high score, it\'s yours for the taking!')

  else:
      print(f'The current high score is {min(attempts_list)} attempts') # The letter 'f' inside a a bracket allows you to add a variable into the print statement.

def start_game():
   attempts = 0
   rand_num = random.randint(1, 10) #randint means a random integer
   print('Hello traveler! Welcome to the game of guesses!')
   player_name = input('What is your name? ')
   wanna_play = input(
       f'Hi, {player_name}, would you like to play the guessing game?'
       '(Enter Yes/No): ')
   
   if wanna_play.lower() != 'yes':
      print('That\'s cool, Thanks!')
      exit()
   else:
       show_score()

   while wanna_play.lower() == 'yes':
       try:
        guess = int(input('Pick a number between 1 and 10: '))
        if guess < 1 or guess > 10:
               raise ValueError(
                   'Please guess a number within the given range')
        attempts += 1
        attempts_list.append(attempts)

        if guess == rand_num:
               print('Nice! You got it!')
               print(f'It took you {attempts} attempts')
               wanna_play = input(
                   'Would you like to play again? (Enter Yes/No): ')
               if wanna_play.lower() != 'yes':
                   print('That\'s cool, have a good one!') # The slash in ' That's ' is just to allow the apostrophe because python only understands alphanumeric values. So the slash just helps the computer to accept the apostrophe.
                   break
               else:
                   attempts = 0
                   rand_num = random.randint(1, 10)
                   show_score()
                   continue
        else:
             if guess > rand_num:
                   print('It\'s lower') # same here with the slash :)
             elif guess < rand_num:
                   print('It\'s higher') # also the same here with the slash... you get idea :)
        


       except ValueError as err:
           print('Oh no!, that is not a valid value. Try again...')
           print(err)


if __name__ == '__main__':
   start_game()

