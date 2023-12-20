import random
import sys

print('----------------------------------------------------------')
print('Hello, Welcome to the Stick Game!')
print('----------------------------------------------------------')

print("")

while True:
    participation = input("Would you like to Play? (yes/no): ")
    if participation.lower() in ["yes", "no"]:
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

if participation.lower() == "yes":
    print('''
    Overview
    This is a simple console-based game where two players take turns removing sticks from a pile."
      "The player who takes the last stick loses the game.

    Each player can take between 1 to 3 sticks at a time. 

    Best of Luck 
    ''')
else:
    print("Thank you. Come again.")
    sys.exit()


def choose_players():
    while True:
        players = int(input("Enter the number of players (1, 2, 0 for 1 vs AI): "))
        if players in [0, 1, 2]:
            return players
        else:
            print("Invalid number of players. Please enter 1, 2, or 0.")

class StickGame:
    def __init__(self, players):
        self.total_sticks = 21
        self.first_player_turn = True
        self.players = players

    def print_sticks(self):
        sticks_out = ""
        stick_numbers = ""
        stick_number = 1
        stick_size = 5

        while stick_size > 0:
            sticks_out += "\n"
            stick_size -= 1

            if self.total_sticks < 9:
                sticks_out += " | " * self.total_sticks
            else:
                sticks_out += " | " * 9
                sticks_out += " |  " * (self.total_sticks - 9)

        while stick_number < self.total_sticks + 1:
            stick_numbers += " {} ".format(stick_number)
            stick_number += 1

        print(sticks_out)
        print(stick_numbers)
        print()

    def take_turn(self):
        player_name = 'Player 1' if self.first_player_turn else 'Player 2'
        sticks_taken = 0

        while sticks_taken < 1 or sticks_taken > 3:
            if self.players == 1 and not self.first_player_turn:
                sticks_taken = random.randint(1, 3 if self.total_sticks > 3 else self.total_sticks)
            else:
                sticks_taken = int(input(player_name + ', make your move: '))

            if sticks_taken > self.total_sticks:
                print('You cannot take more sticks than are left')
                sticks_taken = 0

        self.total_sticks -= sticks_taken
        print("\n{} took {}. There are {} sticks left...".format(player_name, sticks_taken, self.total_sticks))

    def play_game(self):
        while self.total_sticks > 0:
            self.print_sticks()
            self.take_turn()
            self.first_player_turn = not self.first_player_turn

        winner = 'Player 1' if not self.first_player_turn else 'Player 2'
        print(winner + ' you LOST!\n')



def play_again():
    response = input("Would you like to play again? (yes or no): ")
    return response.lower() == "yes"

while True:
    players = choose_players()

    while True:
        game = StickGame(players)
        game.play_game()

        if not play_again():
            break

        # Move choose_players inside the play_again loop
        players = choose_players()

    play_again_choice = input("Do you want to choose players again? (yes or no): ")
    if play_again_choice.lower() != "yes":
        break

print("Thank you, come again.")