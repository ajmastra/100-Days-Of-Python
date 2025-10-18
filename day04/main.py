import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_selection >= 0 and user_selection < 3:
    print(game_images[user_selection])


computer_selection = random.randint(0, 2)

print(f"Computer chose: ")
print(game_images[computer_selection])

if user_selection >= 3 or user_selection < 0:
    print("You typed an invalid number, you lose!")

elif user_selection == 0 and computer_selection == 2:
    print("You win!")

elif computer_selection == 0 and user_selection == 2:
    print("You lose!")

elif computer_selection > user_selection:
    print("You lose!")

elif user_selection > computer_selection:
    print("You win!")

elif computer_selection == user_selection:
    print("It's a draw!")