#importing required lib
import random
from art import *

# Vars
lives = 10
heart_symbol = u'\u2764'
colors = ['R', 'G', 'B', 'W', 'Y']

# Get difficulty input
length = int(input('\nWhat is the length of the secret color (2 / 3 / 4 / 5)? '))

# Prepare the secret color list for guessing
color_list = ''
for i in range(length):
    color_list = color_list + random.choice(colors) 
# Main loop
while (lives > 0):
  print('lives left:' + heart_symbol * lives)
  guess = input('\nWhat is the secret color (R, G, B, W, Y)? ')
  hint_list = ''
  if len(guess) != length:
    print("Please input the secret color with the correct length!")
    break
  for i in range(length):
    if guess[i] == color_list[i]:
      hint_list = hint_list + "*"
    elif guess[i] in color_list:
      hint_list = hint_list + "o"
    else:
      hint_list = hint_list + "X"
  print('Your hints are (* = Black, o = White):' + hint_list)
  if (color_list!= guess):
    lives = lives - 1
    tprint('WRONG!')
  else:
    tprint("CORRECT!")
    break

# End of program