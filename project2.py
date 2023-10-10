# Author: Elvis Ardon
# GitHub username: johnnygitgud
# Date: 10/10/2023
#Description: This program will eventually emulate a Fast Food restaurant. Currently it is a burger customizer.

class BuildaBurger:
  def __init__(self, name):
    """Init method creates with data members one for a name and for an empty list"""
    self._name = name
    self._ingredients = [] #starting with an empty list of ingredients

  def add_ingredient(self, ingredient_name):
    """This method will take add burger ingredients based on user input"""
    self._ingredients.append(ingredient_name)

  def remove_ingredient(self, ingredient_name):
    """This method can remove said ingredients."""
    #This method has not been used yet to interact with the user.
    print("Removing ingredient", ingredient_name)
    self._ingredients.remove(ingredient_name)

  def print_ingredients(self):
    """Method is called to show customer what they wanted on their burger."""
    print("Your burger has:")
    print(self._ingredients)
    return self._ingredients

user_input = ''
#If the user enter n. The loop will continuously ask to help the next customer and greet them.
while user_input != 'y':
  print("Welcome to Build A Burger would you like to Build your own Burger today?")
  user_input = input("Type y for yes or n for no: ")

  if user_input == "y": #When user input is y, the rest of the if statements will execute.
      burger = BuildaBurger("Your Burger") #create an object
      bun_input = input("Would you like a bun? y or n: ")
      
      #These 5 nested if statements will prompt the user to add whast they want on their burger.
      if bun_input != 'n':
        burger.add_ingredient("Bun")
      lettuce_input = input("Would you like lettuce? y or n: ")
      if lettuce_input != 'n':
        burger.add_ingredient("Lettuce")
      tomato_input = input("Would you like to add tomatoes? y or n: ")
      if tomato_input != 'n':
        burger.add_ingredient("Tomatoes")
      cheese_input = input("Would you like to add cheese? y or n: ")
      if cheese_input != 'n':
        burger.add_ingredient("Cheese")
      patty_input = input("Would you like to add a burger patty? y or n: ")
      if patty_input != 'n':
        burger.add_ingredient("Burger Patty")      
      
      burger.print_ingredients() #print a list of what the customer wanted on their burger.
  elif user_input == "n":
    # This condition will loop back to prompt the next customer to customize their burger.
    print("Thank you for stopping buy!\n" "May I help the next guest?")
  else:
      #this condition is for error check if the user enters the wrong character.
      print("Please type y for yes or n for no")

outputfile = open('Burgerfile', 'w')

with open ('Burgerfile', "w") as outputfile:
  outputfile.write(burger.print_ingredients().__str__())