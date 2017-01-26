################################################
### ROCK PAPER SCISSORS (CMPT 120 Assignment #1)
### Date: March 13th 2014
### Team (name and SFU ID):
###   - Fred Mose ( fmose)
################################################


# welcome_prompt(): takes no parameter, prints a welcome
# prompt and the rules.

def welcome_prompt():
  print "WELCOME!"
  print ""
  print "ROCK PAPER SCISSOR in Python"
  print "(Assignment #1 for CMPT 120)"
  print "Author SFU ID: fmose"
  print ""
  print "RULES: 1)Rock beats Scissors, Scissors beats Paper " \
        "and Paper beats Rock"
  print "       2)If both players play the same shape, the game is tied"
  print ""

# get_player_move(): get the users move from the command line

def get_player_move():
  playermove = raw_input("Please choose one of the following \n" \
                   "1) [r]ock, 2) [p]aper, 3) [s]cissors: ")
  playermove = playermove.lower()
  if playermove == "rock" or playermove == "r":
    playermove = 1
    return playermove
  elif playermove == "paper" or playermove == "p":
    playermove = 2
    return playermove
  elif playermove == "scissors" or playermove == "s":
    playermove = 3
    return playermove
  else:
     print "Invalid move! Try again!"
     return get_player_move()

    
# get_computer_move(): gets the computer move

def get_computer_move():
  import random
  compmove = random.randint(1,3)
  if compmove == 1:
    print "Computer played rock"
    return compmove
  elif compmove == 2:
    print "Computer played paper"
    return compmove
  elif compmove == 3:
    print "Computer played scissors"
    return compmove



# compare_moves(): compares the player move and computer move ...
# returns the 1 or -1 or 0 depending on who won or if tied.
  
def compare_moves(playermove, compmove):
  if playermove == compmove:
    return 0
  elif playermove == 1:
    if compmove == 2:
      return -1
    elif compmove == 3:
      return 1
  elif playermove == 2:
    if compmove == 1:
      return 1
    elif compmove == 3:
      return -1
  elif playermove == 3:
    if compmove == 1:
      return -1
    elif compmove == 2:
      return 1
  else:
    return 0


# The rest of the codes below run the whole game by calling the functions above.

  
player_score = 0
comp_score = 0
rounds = 0

welcome_prompt()



while rounds >= 0:
    rounds = rounds +1
    print "ROUND:" , rounds
    playermove = get_player_move()
    compmove = get_computer_move()
    if compare_moves(playermove, compmove) == 1:
        print "Player wins"
        player_score = player_score + 1
    elif compare_moves(playermove, compmove) == -1:
        print "Computer wins"
        comp_score = comp_score + 1
    elif compare_moves(playermove, compmove) == 0:
        print "Tie"
    print "Player score:", player_score, "Computer score:", comp_score, "\n"
    if rounds == 10 and player_score != comp_score:
        break
    if rounds > 10 and player_score != comp_score:
        break
if player_score > comp_score:
     print "THE END: Player wins"
elif comp_score > player_score:
     print "THE END: Computer wins"
     
