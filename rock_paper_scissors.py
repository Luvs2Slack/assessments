import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
choices = ["rock", "paper", "scissors"]    


while True:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    player_choice = str(input("enter a choice of rock, paper or scissors"))
    if player_choice == "rock":
        if computer_choice == "scissors":
            print("you win!")
        elif computer_choice == "paper":
            print("you lose")
        elif computer_choice == "rock":
            print("its a draw")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("you lose")
        elif computer_choice == "rock":
            print("you win")
        elif computer_choice == "paper":
            print("its a draw")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("you lose")
        elif computer_choice == "paper":
            print(" you win")
        elif computer_choice == "scissors":
            print("its a draw")
    else:
        print("invalid choice, pick another choice that is on the list")

    if player_choice == "quit":
        print("thanks for playing")
        break





# Run the game
rock_paper_scissors_game()
