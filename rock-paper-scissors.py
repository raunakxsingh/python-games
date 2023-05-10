# This is the chat gpt version of the game
import random

def get_player_choice():
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    while player_choice not in valid_choices:
        print("Invalid choice, please enter rock, paper, or scissors.")
        player_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    return player_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    win_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if player == computer:
        return "tie"
    elif win_cases.get(player) == computer:
        return "player"
    else:
        return "computer"

player_choice = get_player_choice()
computer_choice = get_computer_choice()
winner = determine_winner(player_choice, computer_choice)

print(f"Your choose {player_choice}, computer choose {computer_choice}")
if winner == "tie":
    print("It's a tie.")
elif winner == "player":
    print("You win!")
else:
    print("You lose.")
