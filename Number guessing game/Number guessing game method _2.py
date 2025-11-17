import random
print("Welcome to the Number Guessing Game!")
print("I will choose 1 number from 1 to 100. You have to guess the number.")
#Generate the random number
secret_number = random.randint(1, 100)
# Debug print - Only for testing
# print(f"(DEBUG) Secret number is: {secret_number")
#Tries count
attempts = 0
while True:
    guess = input("Enter your guess number(1-100): ")
    if not guess.isdigit():
        print("Enter only number!")
        continue
    guess = int(guess)
    attempts += 1
    if guess < secret_number:
        print("Number is too small! Try again.")
    elif guess > secret_number:
        print("Number is too big! Try again.")
    else:
        print(f"Congrats! You guessed the correct number {secret_number} in {attempts} attempts.")
        break