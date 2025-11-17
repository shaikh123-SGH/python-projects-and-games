import random
print("Welcome to the Number Guessing Game!")
print("I will choose 1 number from 1 to 100. You have to guess the number.")
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please!")
        guesses += 1
    elif(a < n):
        print("Higher number please!")
        guesses += 1

print(f"Congratulations! You guessed the correct number {n} in {guesses} attempts.")




