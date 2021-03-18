from art import logo
import random

print(logo)
print("Welcome to Guess My Number Game!\n")
print("I'm thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()


def level_choice(choice):
    if choice == "easy":
        easy_life = 10
        return easy_life
    else:
        hard_life = 5
        return hard_life


level_choosen = level_choice(game_level)


def random_num(length):
    random_number = random.randint(1, int(length * 10))
    return random_number


random_guess = random_num(level_choosen)
print(random_guess)

correct_answer = False
while not correct_answer:

    if level_choosen == 0:
        correct_answer = True
        print("You run out attempts to guess a number")

    else:

        print(f"You have {level_choosen} attempts to guess the number")
        user_guess = int(input("Make a guess.  "))
        if user_guess > random_guess:
            print(' "Too high."')
            print('"Guess again"')
            level_choosen -= 1
        elif user_guess == random_guess:
            print(f"You WIN!!! Answer was {random_guess}")
            correct_answer = True
        else:
            print('"Too low"')
            level_choosen -= 1
