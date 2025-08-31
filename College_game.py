import random

# Function to display instructions
def display_instructions():
    print("=====================================")
    print("   Welcome to Rock-Paper-Scissors!   ")
    print("=====================================")
    print("Rules:")
    print("1 -> Rock")
    print("2 -> Paper")
    print("3 -> Scissors")
    print("4 -> Quit Game")
    print("=====================================")

# Function to get computer's choice
def get_computer_choice():
    return random.randint(1, 3)

# Function to decide winner
def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        return "player"
    else:
        return "computer"

# Function to convert number to choice name
def choice_to_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"

# Main function
def play_game():
    player_score = 0
    computer_score = 0

    display_instructions()

    while True:
        try:
            player = int(input("Enter your choice (1/2/3 or 4 to quit): "))
        except():
            print("Invalid input! Please enter a number (1-4).")
            continue

        if player == 4:
            print("Thanks for playing! Final Score:")
            print(f"Player: {player_score} | Computer: {computer_score}")
            break

        if player not in [1, 2, 3]:
            print("Invalid choice! Enter 1, 2, 3 or 4.")
            continue

        computer = get_computer_choice()
        print(f"You chose: {choice_to_name(player)}")
        print(f"Computer chose: {choice_to_name(computer)}")

        result = decide_winner(player, computer)
        if result == "tie":
            print("Such an srm behaviour!! ")
        elif result == "player":
            print("Congratulations for  winning a cupon in java !! ")
            player_score += 1
        else:
            print("AI took over you !!! ")
            computer_score += 1

        print(f"Current Score -> Player: {player_score}, Computer: {computer_score}")
        print("---------------------------------------------------")

# Run the game
play_game()
