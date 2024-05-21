import random

def get_user_choice():
    """Get user's choice (rock, paper, or scissors)."""
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
