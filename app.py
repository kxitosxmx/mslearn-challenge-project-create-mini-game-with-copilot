import random

def get_computer_choice():
    """Randomly selects between 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the round."""
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_results(player_choice, computer_choice, result):
    """Displays the results of the round."""
    print(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    if result == 'win':
        print("You win this round!")
    elif result == 'lose':
        print("You lose this round.")
    else:
        print("It's a tie!")

def play_game():
    """Runs the Rock-Paper-Scissors game."""
    wins = 0
    rounds = 0

    while True:
        # Player input
        player_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()

        # Input validation
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer choice
        computer_choice = get_computer_choice()

        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        display_results(player_choice, computer_choice, result)

        # Update score
        rounds += 1
        if result == 'win':
            wins += 1

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    # Final score display
    print(f"\nGame over! You won {wins} out of {rounds} rounds.")

if __name__ == "__main__":
    play_game()
