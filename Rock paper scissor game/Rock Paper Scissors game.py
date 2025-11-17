import random

print("Welcome to Rock Paper Scissor!")

choices = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter rock, paper or scissor (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("Thank for playing! Bye!")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
            print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissor")
        or (user_choice == "paper" and computer_choice == "rock")
        or(user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

        
