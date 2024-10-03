import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Type 'quit' to exit.")

    user_score = 0
    computer_score = 0

    while True:
        # User Input
        user_input = input("Enter your choice (1, 2, 3): ")
        if user_input == 'quit':
            break
        if user_input not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        # Map user input to choice
        choices_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = choices_map[user_input]

        # Computer Selection
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Play Again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    main()