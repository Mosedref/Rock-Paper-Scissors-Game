################################################
### ROCK PAPER SCISSORS(CMPT 120 Assignment #1)
### Date:
### Team (name and SFU ID):
###   - Fred Mose, fmose
################################################
### Advanced tasks:
### - additional weapons (spock and lizard)
################################################


# welcome_prompt(): takes no parameter, prints a welcome
# prompt and the rules.

def welcome_prompt():
  print "WELCOME!\n"
  print "ROCK PAPER SCISSOR SPOCK LIZARD in Python"
  print "(Assignment #1 for CMPT 120)"
  print "Author SFU ID: fmose"
  print ""
  print "RULES: 1)- Rock beats Scissors and Lizard " \
                " \n         - Paper beats Rock and Spock"\
                " \n         - Scissors beats Paper and Lizard " \
                " \n         - Spock beats Rock and Scissors" \
                " \n         - Lizard beats Spock and Paper" \
                " \n       2)If both players throw the same shape," \
                "the game is tied \n"



def get_player_move():
  playermove = raw_input("Please choose one of the following \n" \
                   "1) [r]ock, 2) [P]aper, 3) [s]cissors 4) [L]izard " \
                         "5) [sp]ock:")
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
  elif playermove == "lizard" or playermove == "l":
    playermove = 4
    return playermove
  elif playermove == "spock" or playermove == "sp":
    playermove = 5
    return playermove
  else:
     print "Invalid move! Try again!"
     return get_player_move()

    

def get_computer_move():
  import random
  compmove = random.randint(1,5)
  if compmove == 1:
    print "Computer played rock"
    return compmove
  elif compmove == 2:
    print "Computer played paper"
    return compmove
  elif compmove == 3:
    print "Computer played scissors"
    return compmove
  elif compmove == 4:
    print "Computer played lizard"
    return compmove
  elif compmove == 5:
    print "Computer played spock"
    return compmove




def compare_moves(playermove, compmove):
  if playermove == compmove:
    return 0
  elif playermove == 1:
    if compmove == 2 or compmove == 5:
      return -1
    elif compmove == 3 or compmove == 4:
      return 1
  elif playermove == 2:
    if compmove == 1 or compmove == 5:
      return 1
    elif compmove == 3 or compmove == 4:
      return -1
  elif playermove == 3:
    if compmove == 1 or compmove == 5:
      return -1
    elif compmove == 2 or 4:
      return 1
  elif playermove == 4:
    if compmove == 2 or compmove == 5:
      return 1
    elif compmove == 1 or compmove == 3:
      return -1
  elif playermove == 5:
    if compmove == 1 or compmove == 3:
      return 1
    if compmove == 2 or compmove == 4:
      return -1
  else:
    return 0



playerscore = 0
compscore = 0
rounds = 0
welcome_prompt()
while rounds >= 0:
    rounds = rounds +1
    print "ROUND:" , rounds
    playermove = get_player_move()
    compmove = get_computer_move()
    if compare_moves(playermove, compmove) == 1:
        print "Player wins"
        playerscore = playerscore + 1
    elif compare_moves(playermove, compmove) == -1:
        print "Computer wins"
        compscore = compscore + 1
    elif compare_moves(playermove, compmove) == 0:
        print "Tie"
    print "Player score:", playerscore, "Computer score:", compscore, "\n"
    if rounds == 10 and playerscore != compscore:
        break
    if rounds > 10 and playerscore != compscore:
        break
if playerscore > compscore:
     print "THE END: Player wins"
elif compscore > playerscore:
     print "THE END: Computer wins"
    
