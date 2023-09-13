import random

class RockPaperScissors:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.current_round = 0
        self.player_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        choices = ['Rock', 'Paper', 'Scissors']
        return random.choice(choices)

    def find_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'Tie'
        elif (
            (player_choice == 'Rock' and computer_choice == 'Scissors') or
            (player_choice == 'Paper' and computer_choice == 'Rock') or
            (player_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            return 'Player'
        else:
            return 'Computer'

    def play_round(self, player_choice):
        computer_choice = self.get_computer_choice()
        result = self.find_winner(player_choice, computer_choice)
        if result == 'Player':
            self.player_wins += 1
        elif result == 'Computer':
            self.computer_wins += 1
        self.current_round += 1
        return result

    def game_over(self):
        return self.current_round >= self.num_rounds

    def get_game_result(self):
        if self.player_wins > self.computer_wins:
            return 'Player wins!'
        elif self.computer_wins > self.player_wins:
            return 'Computer wins!'
        else:
            return 'It\'s a tie!'

    def play_game(self):
        while not self.game_over():
            print(f"Round {self.current_round + 1}/{self.num_rounds}")
            player_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
            if player_choice not in ['Rock', 'Paper', 'Scissors']:
                print("Invalid choice. Please choose Rock, Paper, or Scissors.")
                continue
            result = self.play_round(player_choice)
            print(f"Computer chose: {self.get_computer_choice()}")
            if result == 'Tie':
                print("It's a tie for this round.")
            else:
                print(f"{result} wins this round.")
            print(f"Player: {self.player_wins} - Computer: {self.computer_wins}\n")
        
        print(self.get_game_result())

# Example usage:
num_rounds = 3
game = RockPaperScissors(num_rounds)
game.play_game()
