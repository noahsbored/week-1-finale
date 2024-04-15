import random

# Define days of the week and meals
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
meals = ['Breakfast', 'Lunch', 'Dinner']

# Generate a random meal plan for each day of the week
for day in days_of_week:
    print("Meal Plan for", day + ":")
    for meal in meals:
        food = random.choice(['Eggs', 'Toast', 'Oatmeal', 'Salad', 'Sandwich', 'Pizza', 'Stir-fry', 'Burger', 'Pasta', 'Soup'])
        print(meal + ": " + food)
    print()  # Print an empty line to separate meal plans for different days
