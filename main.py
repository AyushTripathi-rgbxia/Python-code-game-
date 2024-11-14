
# Online Python - IDE, Editor, Compiler, Interpreter

import random

def get_user_choice():
    # Get user input, and ensure it's valid
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    # Randomly choose between rock, paper, or scissors
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
