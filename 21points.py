import random
import time
cards = [i for i in range(1,12)]
computer = []
player = []


def draw_card(p=player):
    x = random.choice(cards)
    cards.remove(x)
    p.append(x)
    x = random.choice(cards)


def start_game(user_name):
    time.sleep(3)
    print('READY?')
    time.sleep(1)
    print('SET,')
    time.sleep(1)
    print('GO!')
    time.sleep(1)
    n = 0


    while n <= 1:
        draw_card()
        draw_card(computer)
        n = n + 1


    print("computer's card: **",computer[1:])
    print('='*100)
    print(user_name,':',player)
    player_input = input('Do you want to draw card? -(Yes or No)')
    while sum(computer) <= 16 or (player_input == 'Yes' and sum(player) < 21):
        if sum(computer) <= 16:
            draw_card(computer)
            print('computer draws a card')
            print("computer's card: **", computer[1:])
        elif player_input == 'Yes':
            draw_card()
            print(user_name,':',player)
            player_input = input('Do you want to draw card? -(Yes or No)')


    print('Show cards!')
    print("computer's card:",computer)
    print('='*100)
    print(user_name,':',player)


    # whether player win or not
    if sum(computer) <= 21 and sum(player) <= 21:
        if sum(computer) < sum(player):
            print('YOU WIN!')
        elif sum(computer) == sum(player):
            print('The score is tied')
        else:
            print('YOU LOSE!')
    elif sum(computer) > 21 and sum(player) > 21:
        if sum(computer) > sum(player):
            print('YOU WIN!')
        elif sum(computer) == sum(player):
            print('The score is tied')
        else:
            print('YOU LOSE!')
    elif sum(computer) > 21 and sum(player) <= 21:
        print('YOU WIN!')
    else:
        print('YOU LOSE!')
    print("Thanks for playing and thank dusmart's help!")


print("21点游戏:每轮你可以选择抽牌或不抽，最后点数最接近且不超过21的胜利（牌堆里有1到11的牌且每种牌只有一张）")
start_game('TBZmang')
