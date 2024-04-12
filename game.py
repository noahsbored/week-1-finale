import random

items = ["apple", "banana", "orange", "grape", "pear"]

selected_item = random.choice(items)

while True:
    guess = input("Guess which item was selected: ")

    if guess.lower() == selected_item:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Sorry, that's incorrect. Try again.")
