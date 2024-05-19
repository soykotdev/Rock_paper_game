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
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game=[rock , paper , scissors]

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))



computer_choice=random.randint(0,2)


if choice>=3:
   print(" You input wrong numbers")
elif choice==0 and computer_choice==2:
    print(f" Your choose is \n {game[choice]}")
    print(f"Computer choice {game[computer_choice]}")
    print(" You Win")
elif computer_choice==0 and choice==2:
    print(f" Your choose is \n {game[choice]}")
    print(f"Computer choice {game[computer_choice]}")
    print(" You lose")
elif choice==1 and computer_choice==0:
    print(f" Your choose is \n {game[choice]}")
    print(f"Computer choice {game[computer_choice]}")
    print(" You Win")
elif choice==0 and computer_choice==1:
    print(f" Your choose is \n {game[choice]}")
    print(f"Computer choice {game[computer_choice]}")
    print(" You lose")
elif computer_choice==choice:
    print(f" Your choose is \n {game[choice]}")
    print(f"Computer choice {game[computer_choice]}")
    print(" It's tie")
else:
    print(f" Your choose is \n {game[choice]}")

    print(f"Computer choice {game[computer_choice]}")
    print(" You Lose")









