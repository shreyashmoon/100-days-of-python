import random 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

sissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

Ascii_art = [rock, paper, sissor]

user = int(input("What is you choice? 0 for rock, 1 for paper and 2 for sissor: \n"))
if user > 2 or user < 0:
    print("Invalid input")
else:
    print(f"User choose:{Ascii_art[user]}")    
Computer = random.randint(0,2)
print(f"Computer choose:{Ascii_art[Computer]}")



if user == Computer:
    print("DRAW")
elif user == 1 and Computer == 0:
    print("User Wins")
elif user == 0 and Computer == 2:
    print("User wins")
elif user == 2 and Computer == 1:
    print("User Wins")
else:
    print("Computer Wins")


