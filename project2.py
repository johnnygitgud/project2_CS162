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
        #print(burger.add_ingredient) #This confirms the memory address for where the ingredient is being stored.
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

      #burger.print_ingredients() # Test print a list of what the customer wanted on their burger.
  elif user_input == "n":
    # This condition will loop back to prompt the next customer to customize their burger.
    print("Thank you for stopping buy!\n" "May I help the next guest?")
  else:
      #this condition is for error check if the user enters the wrong character.
      print("Please type y for yes or n for no")

# Code for writing the list to a file called Burgerfile
# Issue with this code is that each time we run the program it overwrites the previous list/
outputfile = open('Burgerfile', 'w')

with open ('Burgerfile', "w") as outputfile:
  outputfile.write(burger.print_ingredients().__str__())
  outputfile.write("\n")



#Tests for that are intended to either break or prove the Buildaburger class works.
# As of 10/11/2023 There is an usse with the ingredient questions.
# There is no input validation when anyting is entered other thatn 'n'.
#That means a complete burger ingredient list will be printed when the user enters bogus input after they answer 'y' to the first question.


#This test is a negative test. It breaks the program when the user successfully creats their burger list.
# print(f"userinput: {user_input}")
# print(f"userinput {user_input == True}")
# while True: #Use an infinite loop
#   if user_input == True: # Only after the first question is answered as y will this loop cause a crash.
#   # Once the list is completed we can't rerun the program without a keyboardinterrupt.
#   # From my under it doesn't matter when user input is set to true or false in lines 77 and 79.
#   #This is a contradiction because it is true that the user is entering y. But its not being evaluated that way.
#   # This is probably because userinput was never initialized to a boolean data type.
#     x = 2
#     print(x)