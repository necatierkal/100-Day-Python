import art
import game_data
import random

print(art.logo)

def random_famous_find():
    random_number = random.randint(0, 49)
    random_A = game_data.data[random_number]
    return random_A

def compare(a,b,c):
    if a['follower_count']>b['follower_count'] and c=='A':
        return True
    elif a['follower_count']<b['follower_count'] and c=='B':
        return True
    else:
        return False

def start_print():
    print(f"Compare A: {famous_a['name']} , a {famous_a['description']}, from  {famous_a['country']}")
    print(art.vs)
    print(f"Against B: {famous_b['name']} , a {famous_b['description']}, from  {famous_b['country']}")

famous_a = random_famous_find()
famous_b = random_famous_find()

start_print()
user_answer = input("Who has more followers? Type 'A' or 'B' :").upper()

consequence = compare(famous_a, famous_b, user_answer)
count=0
while consequence:
    count+=1
    print(f"You're right! Current score: {count}.")
    famous_a=famous_b
    famous_b = random_famous_find()
    start_print()
    user_answer = input("Who has more followers? Type 'A' or 'B' :").upper()
    consequence = compare(famous_a, famous_b, user_answer)

print(f"Sorry, that's wrong. Final score : {count}")