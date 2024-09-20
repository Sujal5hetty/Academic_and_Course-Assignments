#PROBLEM STATEMENT:
#Rock, paper, scissors is a game played by two participants. The game consists of rounds. In each round, a participant chooses a symbol from rock, paper, or scissors,
#and the other participant does the same. Then a winner of the round is determined by comparing the chosen symbols.
#The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock.
#The winner of the round is awarded a point. The game goes on for as many rounds as the participants agree on. The winner is the participant with the most points.










import random

# Define a class for Player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None
    
    # Method for player to make a choice
    def make_choice(self):
        choices = ['rock', 'paper', 'scissors']
        self.choice = random.choice(choices)
        return self.choice

# Define a class for the Game
class Game:
    def __init__(self, player1, player2, rounds):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds
    
    # Method to determine winner of a round
    def determine_winner(self, choice1, choice2):
        if choice1 == choice2:
            return None
        elif (choice1 == 'rock' and choice2 == 'scissors') or \
             (choice1 == 'scissors' and choice2 == 'paper') or \
             (choice1 == 'paper' and choice2 == 'rock'):
            return self.player1
        else:
            return self.player2
    
    # Method to play the game
    def play(self):
        for round_num in range(1, self.rounds + 1):
            print(f"\nRound {round_num}:")
            choice1 = self.player1.make_choice()
            choice2 = self.player2.make_choice()
            print(f"{self.player1.name} chooses {choice1}")
            print(f"{self.player2.name} chooses {choice2}")
            
            winner = self.determine_winner(choice1, choice2)
            if winner:
                winner.score += 1
                print(f"{winner.name} wins this round!")
            else:
                print("It's a tie!")
        
        # Determine overall winner
        if self.player1.score > self.player2.score:
            print(f"\n{self.player1.name} wins the game with {self.player1.score} points!")
        elif self.player2.score > self.player1.score:
            print(f"\n{self.player2.name} wins the game with {self.player2.score} points!")
        else:
            print("\nThe game is a tie!")

# Example of how to use the classes
player1 = Player("Player 1")
player2 = Player("Player 2")

rounds = int(input("Enter number of rounds: "))
game = Game(player1, player2, rounds)
game.play()
