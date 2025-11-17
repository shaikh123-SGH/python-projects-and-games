import random
def get_computer_choice():
    choice = random.choice(['s', 'w', 'g'])
    print(f"[DEBUG] Computer randomly chose: {choice}")
    return choice
def get_result(user, computer):
    if user == computer:
        return "Draw"
    elif (user == 's' and computer == 'w') or \
         (user == 'w' and computer == 'g') or \
         (user == 'g' and computer == 's'):
        return "You Win!"
    else:
        return "You Lose!"
def play_game():
    print("Welcome to Snake Water Gun Game!")
    print("Rules: s = Snake, w = Water, g = Gun")
    user_score = 0
    comp_score = 0
    for round_num in range(1, 6):
        print(f"Round {round_num}")
        user_choice = input("Enter your choice (s,w,g): ").lower()
        if user_choice not in ['s', 'w', 'g']:
            print("Invalid input. Try again!")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = get_result(user_choice, computer_choice)
        print(result)
        if result == "You Win!":
            user_score += 1
        elif result == "You Lose!":
            comp_score += 1
    print("\nFinal Scores: ")
    print(f"You: {user_score} | Computer: {comp_score}")
    if user_score > comp_score:
        print("Congratulations! You won the game.")
    elif user_score < comp_score:
        print("Sorry! You lost the game.")
    else:
        print("It's a Draw!")
play_game()
    