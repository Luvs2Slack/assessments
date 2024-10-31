import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
choices = ["rock", "paper", "scissors", "lizard", "spock"]    


while True:
    computer_choice = random.choice(choices)
    
    
    player_choice = str(input("enter a choice of rock, paper, scissors, lizard or spock "))
    if player_choice == "rock":
        if computer_choice == "scissors":
            print("you win!")
        elif computer_choice == "paper":
            print("you lose")
        elif computer_choice == "rock":
            print("its a draw")
        elif computer_choice == "lizard":
            print("you win")
        elif computer_choice == "spock":
            print("you lose")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("you lose")
        elif computer_choice == "rock":
            print("you win")
        elif computer_choice == "paper":
            print("its a draw")
        elif computer_choice == "lizard":
            print("you lose")
        elif computer_choice == "spock":
            print("you win")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("you lose")
        elif computer_choice == "paper":
            print(" you win")
        elif computer_choice == "scissors":
            print("its a draw")
        elif computer_choice == "lizard":
            print("you win")
        elif computer_choice == "spock":
            print("you lose")
    elif player_choice == "spock":
        if computer_choice == "rock":
            print("you win")
        elif computer_choice == "paper":
            print("you lose")
        elif computer_choice == "scissors":
            print("you win")
        elif computer_choice == "lizard":
            print("you lose")
        elif computer_choice == "spock":
            print("its a draw")
    elif player_choice == "lizard":
        if computer_choice == "rock":
            print("you lose")
        elif computer_choice == "paper":
            print("you win")
        elif computer_choice == "scissors":
            print("you lose")
        elif computer_choice == "spock":
            print("you win")
        elif computer_choice == "lizard":
            print("its a draw")

    
    
    if player_choice == "quit":
        print("thanks for playing")
        break





# Run the game
rock_paper_scissors_game()
