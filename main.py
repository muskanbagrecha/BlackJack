from art import logo
from random import choice
import os
from time import sleep
cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

def deal(player):
    """
    This function deals a card to the player. 
    """
    card = choice(cards)
    return player.append(card)

def calculate_score(player):
    """
    This function calculates the score of the player. Returns score
    """
    sum=0
    for i in player:
        if i=='J' or i=='Q' or i=='K':
            sum+=10
        elif i == 'A':
            sum+=11
            if sum>21:
                sum=sum-11+1
        else:
            sum+=i
    return sum

def show(player):
    """
    This function is used to display the cards held by the player. It also displays the score. 
    """
    print(f"Your cards: {player}, current score: {calculate_score(player)}")

def compare(user, comp, user_score, comp_score):
    """
    This function determines the winner of the game based on the scores. 
    """
    if comp_score==21 and len(comp)==2:
        print("Bot has a Golden BlackJack. You lose!!")
    elif user_score==21 and len(user)==2:
        print("You have a Golden BlackJack. You win!!")
    elif comp_score==21 and user_score==21:
        print("Draw! Both have BlackJack!")
    elif comp_score==21:
        print("You lose! Bot has a BlackJack!")
    elif user_score==21:
        print("You win! You have a BlackJack!")
    elif comp_score>21 and user_score>21:
        print("It is a draw! Both are over 21")
    elif comp_score>21:
        print("You win! Bot went over 21")
    elif user_score>21:
        print("You lose! You went over 21")
    elif user_score==comp_score:
        print("It is a draw!")
    elif comp_score>user_score:
        print("You lose! Bot scored more than you.")
    else: print("You win! You scored more than the bot.")

def game():
    """This function runs the blackjack game"""
    user=[]
    comp=[]
    user_score=0
    comp_score=0
    for i in range(2):
        deal(user)
        deal(comp)
    user_score=calculate_score(user)
    comp_score=calculate_score(comp)    
    show(user)
    print(f"Bot's first card: {comp[0]}")
    while(True):
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_game=='y':
            deal(user)
            user_score=calculate_score(user)
            show(user)
        else:
            break
    while(comp_score<=16):
        deal(comp)
        comp_score=calculate_score(comp)
    print(f"Your final hand: {user}, score: {user_score}")
    print(f"Bot's final hand: {comp}, score: {comp_score}")
    compare(user, comp, user_score,comp_score)

        
while(True):
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play =='y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        game()
        sleep(10)
    else:
        print("Thank You!")
        break
