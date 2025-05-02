import random 

def rock_paper_scissor():
    options = ["rock","paper","scissor"]


    while True:
        user_choice = input('chooose the option: rock, paper or scissor ').lower() # convert to lower case
        
        if user_choice not in options:
            print("Wrong option: choose correct option")
            continue
        
        computer_choice = random.choice(options)

        print(f"Computer choose: {computer_choice}")
        print(f"User choose: {user_choice}")


        if user_choice == computer_choice:
            print("It's a tie, try again")
        elif (user_choice == "rock" and computer_choice == "scissor") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissor" and computer_choice == "paper"):
            print("You Win :)")

        else:
            print("computer win :)")

        play_again = input("Want to try your luck again ? (yes/no)").strip().lower()
        if play_again == "yes":
            print("Cool")
            continue
        elif play_again == "no":
            print("Alright, Thanks for playing")
            break
        else:
            print("Please answer with 'yes' or 'no'")
if __name__ == "__main__":
    rock_paper_scissor()