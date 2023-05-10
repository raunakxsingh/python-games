# This version is the chatgpt refactored version of my code 
import random

def get_choices():
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return player_choice, computer_choice

def check_win(player, computer):
    win_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if player == computer:
        return "It's a tie"
    elif win_cases.get(player) == computer:
        return f"{player} beats {computer}! You win."
    else:
        return f"{computer} beats {player}. You lose."

player_choice, computer_choice = get_choices()
result = check_win(player_choice, computer_choice)
print(f"Your choose {player_choice}, computer choose {computer_choice}")
print(result)
