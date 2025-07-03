import random

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
       ___________)
      (____)
---.__(___)
'''

user_input=int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 For Scissors.\n"))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
else:
    print(scissors)
computer_chose=random.randint(0,2)
print(f"Computer chose: {computer_chose}")
if computer_chose == 0:
    print(rock)
elif computer_chose == 1:
    print(paper)
else:
    print(scissors)
if  computer_chose<user_input:
    print("user won!")
elif computer_chose<user_input:
    print("You lost!")
elif user_input==computer_chose:
    print("Offo, tie case!")
else:
    print("Computer Won!")

