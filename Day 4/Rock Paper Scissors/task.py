
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

game_array = [rock,paper,scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("Ne seçmek istersiniz? Taş için 0, Kağıt için 1, Makas için 2 yaz...\n"))

print("Senin Seçimin:\n")
if user_choice >=0 and user_choice <= 2:
    print(game_array[user_choice])
print("\nBilgisayarın Seçimi:\n")
print(game_array[computer_choice])

if user_choice>=3 or user_choice <0:
    print("Lütfen 0,1 ya da 2 giriniz.")
elif user_choice == 0 and computer_choice == 2:
    print("Kazandın!")
elif computer_choice == 0 and user_choice == 2:
    print("Kaybettin!")
elif computer_choice > user_choice:
    print("Kaybettin!")
elif user_choice > computer_choice:
    print("Kazandın!")
elif computer_choice == user_choice:
    print("Berabere!")




