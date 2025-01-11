# import random
# import art
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# want_to_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# final_hand_user =[]
# final_hand_computer =[]
# final_score_user = 0
# final_score_computer = 0
#
#
# def add_cards(how_many_card):
#     global final_score_user, final_score_computer
#     for item in range(how_many_card):
#         number1 = int(random.choice(cards))
#         number2 = int(random.choice(cards))
#         final_hand_user.append(number1)
#         final_score_user += number1
#         if final_score_computer <=16:
#             final_hand_computer.append(number2)
#             final_score_computer += number2
#     return final_score_user,final_score_computer
#
# add_cards(2)
#
# def compare(final_hand_user,final_hand_computer,final_score_user,final_score_computer):
#     print(f"Your final hand: {final_hand_user}, final score: {final_score_user}")
#     print(f"Computer's final hand: {final_hand_computer}, final score: {final_score_computer}")
#     if final_score_user > final_score_computer and final_score_user <=21:
#         print("You win")
#     if final_score_user < final_score_computer and final_score_computer <= 21:
#         print("You loose")
#     if final_score_user>21:
#         print("You went over. You loose")
#     if final_score_computer>21:
#         print("Opponent went over. You win.")
#     if final_score_computer == final_score_user:
#         print("Draw")
#
#
# if want_to_play == 'y':
#     print(art.logo)
#     print(f"Your cards: {final_hand_user}, current score: {final_score_user}")
#     print(f"Computer's first card: {final_hand_computer[0]}")
#     add_cart= True
#     while add_cart :
#         get_card= input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         if get_card == 'y':
#             add_cards(1)
#             print(f"Your cards: {final_hand_user}, current score: {final_score_user}")
#             print(f"Computer's first card: {final_hand_computer[0]}")
#         else:
#             add_cart = False
#     compare(final_hand_user,final_hand_computer,final_score_user,final_score_computer)
# #
# # else:
# #     print(f"Your final hand: {final_hand_user}, final score: {final_score_user}")
# #     print(f"Computer's final hand: {final_hand_computer}, final score: {final_score_computer}")
#
#
#
from random import random


###############################Version 2 #############################################
# import random
# import art
#
# # Kart değerleri
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# # Kullanıcıya oyunu oynayıp oynamak istediğini sor
# def play_blackjack():
#     want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if want_to_play == 'y':
#         print(art.logo)
#         game()
#     else:
#         print("Maybe next time!")
#
#
# # Yeni kart çekme fonksiyonu (As'ı kontrol eder)
# def draw_card(hand, current_score):
#     card = random.choice(cards)
#     if card == 11 and current_score + 11 > 21:
#         card = 1  # As'ı 1 olarak kullan
#     hand.append(card)
#     return current_score + card
#
#
# # Kullanıcının ve bilgisayarın ellerini başlatır
# def initialize_hands():
#     user_hand = []
#     computer_hand = []
#     user_score = draw_card(user_hand, 0)
#     user_score = draw_card(user_hand, user_score)
#     computer_score = draw_card(computer_hand, 0)
#     computer_score = draw_card(computer_hand, computer_score)
#     return user_hand, computer_hand, user_score, computer_score
#
#
# # Kart durumunu göster
# def display_status(user_hand, user_score, computer_hand):
#     print(f"Your cards: {user_hand}, current score: {user_score}")
#     print(f"Computer's first card: {computer_hand[0]}")
#
#
# # Oyuncunun kart çekip çekmeyeceğini belirler
# def user_turn(user_hand, user_score):
#     while user_score < 21:
#         action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         if action == 'y':
#             user_score = draw_card(user_hand, user_score)
#             print(f"Your cards: {user_hand}, current score: {user_score}")
#         else:
#             break
#     return user_score
#
#
# # Bilgisayarın kart çekme stratejisi
# def computer_turn(computer_hand, computer_score):
#     while computer_score <= 16:
#         computer_score = draw_card(computer_hand, computer_score)
#     return computer_score
#
#
# # Sonucu karşılaştır ve kazananı belirle
# def compare_scores(user_score, computer_score):
#     if user_score > 21:
#         return "You went over. You lose!"
#     elif computer_score > 21:
#         return "Opponent went over. You win!"
#     elif user_score > computer_score:
#         return "You win!"
#     elif user_score < computer_score:
#         return "You lose!"
#     else:
#         return "It's a draw!"
#
#
# # Oyunun ana akışı
# def game():
#     user_hand, computer_hand, user_score, computer_score = initialize_hands()
#     display_status(user_hand, user_score, computer_hand)
#
#     # Kullanıcının sırası
#     user_score = user_turn(user_hand, user_score)
#
#     # Bilgisayarın sırası (kullanıcı aşmadıysa)
#     if user_score <= 21:
#         computer_score = computer_turn(computer_hand, computer_score)
#
#     # Son durum
#     print(f"\nYour final hand: {user_hand}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
#     print(compare_scores(user_score, computer_score))
#
#
# # Oyunu başlat
# play_blackjack()


###############################Version 3 #############################################
import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return  0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score >21:
        return "You went over. Yo lose"
    elif c_score >21:
        return "Opponent went over. You win"
    elif u_score>c_score:
        return  "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=='y':
    print("\n"*20)
    play_game()