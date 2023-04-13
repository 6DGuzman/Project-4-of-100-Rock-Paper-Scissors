import random

# Instructions
# Make a rock, paper, scissors game.
# Inside the `main.py` file, you'll find the ASCII art for the ' \
# hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`.
# This will make it easy to print them out to the console.
# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out:
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]
player = int(input("Rock, Paper, Scissors. Type 0 for Rock, 1 for Paper, and 2 Scissors.\n"))
print("Player chose:\n")
print(options[player])

comp_choice = random.randint(0, 2)
print("Computer chose:\n")
print(options[comp_choice])

if player >= 3 or player < 0:
    print("Out of range, you lose")
elif player == 0 and comp_choice == 2:
    print("You Win!")
elif comp_choice == 0 and player == 2:
    print("You Lose!")
elif comp_choice > player:
    print("You Lose!")
elif player > comp_choice:
    print("You Win!")
elif player == comp_choice:
    print("It's a Tie!")
# Solution
# 1. Ask the user (player), since we need it as an integer value for rock, paper, scissors, case it as an int.
# 2. Encapsulate the options for rock, paper, scissors into one variable and create a list (options).
# 2a. Keep the list at the very top to be triggered first.
# 3. Print function for both player and computer to trigger image to be printed.
# 4. Set a variable for computer to use the random function.
# 5. If statement that captures what happens if a player chooses a number outside the range of 0, 1, and 2.
# 6. Set variable (computer) to equal random and randint (random number between 0 and 2.)
# 7. Print function for computer to display number chosen with corresponding ascii image.
# 8. IMPORTANT: Have an if statement that gets triggered underneath the player input if a player chooses
# 8a. A number that is outside the range of the given options
# 9. An else to complete the loop that enables program to move in if player chooses a valid number.
# 10. AFTER computer randomization:
# 11. If statement(s) that covers all possible outcomes of the rock, paper, and scissors game.
# 12. Tabbing is EXTREMELY important, ensure all tabs are correctly placed.
# 13. Case in point, when creating a new If statement underneath an already existing if statement.
# 13a. Those are only TRUE and executed if tabbed correctly with the if statements placed below an existing.
# 13b. If statement.
