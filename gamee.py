import random

def random_choice_game(items):
 
    selected_item = random.choice(items)
    
    while True:
      
        guess = input("Guess which item was selected: ")
        

        if guess == selected_item:
            print("you guessed it")
            break
        else:
            print("nope")


items = ['apple', 'banana', 'orange', 'grape', 'pear']


random_choice_game(items)
