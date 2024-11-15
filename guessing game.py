import random

number_to_guess = random.randint(1, 100) #random number is chosen

#Loops until the riight number is guessed, gives hints as higher or lower
while True:
    guess = int(input("Enter your guess: "))
    if guess < number_to_guess:
        print("Higher!")
    elif guess > number_to_guess:
        print("Lower!")
    else:
        print(f"Congratulations! You've guessed the number.")
        break
