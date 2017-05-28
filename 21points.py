import random
import time
put_back = 1
points = 0
bombs = 0
started = False


def start_game(user_name):
    global points
    global put_back
    global bombs
    global started
    cards = [i for i in range(1, 12)]
    player = []
    computer = []
    if not started:
        print("21点游戏:每轮你可以选择抽牌或不抽，最后点数最接近且不超过21的胜利（牌堆里有1到11的牌且每种牌只有一张）")
        time.sleep(3)
    print('READY?')
    time.sleep(1)
    print('SET,')
    time.sleep(1)
    print('GO!')
    time.sleep(1)
    n = 0


    def draw_card(p=player):
        x = random.choice(cards)
        cards.remove(x)
        p.append(x)
        x = random.choice(cards)

    def put_card_back(p=player):
        cards.append(p[-1])
        p.remove(p[-1])


    def blow_up(p=computer):
        cards.append(p[-1])
        p.remove(p[-1])


    def buy_bomb():
        InputResult = input('Do you want to buy a bomb? -(Yes or No)')
        global points
        global bombs
        if InputResult == 'Yes':
            if points >= 2000:
                points = points - 2000
                bombs = bombs + 1
                print('You have',points,'points')
                buy_bomb()
            else:
                print('Your points is not enough!')
        elif InputResult == 'No':
            pass


    def buy_bonus():
        InputResult = input('Do you want to buy a put-back? -(Yes or No)')
        global points
        global put_back
        if InputResult == 'Yes':
            if points >= 1500:
                points = points - 1500
                put_back = put_back + 1
                print('You have',points,'points')
                buy_bonus()
            else:
                print('Your points is not enough!')
        elif InputResult == 'No':
            pass


    while n <= 1:
        draw_card()
        draw_card(computer)
        n = n + 1


    #draw card and put back
    print("computer's card: **",computer[1:],'the sum of them are(not with hided num)',sum(computer[1:]))
    print()
    print('='*100)
    print()
    print(user_name+'\'s card:',player,'the sum of them are',sum(player))
    player_input = input('Do you want to draw card? -(Yes,No,putBack or bomb)')
    while ((sum(computer) <= 16 or player_input == 'Yes') or player_input == 'putBack') or player_input == 'bomb':
        if sum(computer) <= 16:
            draw_card(computer)
            print('computer draws a card')
            print("computer's card: **",computer[1:],'the sum of them are(not with hided num)',sum(computer[1:]))
        elif player_input == 'Yes':
            draw_card()
            print(user_name+'\'s card:',player,'the sum of them are',sum(player))
            player_input = input('Do you want to draw card? -(Yes,No or putBack)')
        elif player_input == 'putBack':
            if put_back > 0:
                put_card_back()
                put_back = put_back - 1
                print(user_name+'\'s card:',player,'the sum of them are',sum(player))
            else:
                'You haven\'t any put-backs left!'
        elif player_input == 'bomb':
            if bombs > 0:
                blow_up()
                bombs = bombs - 1
                print("computer's card: **",computer[1:],'the sum of them are(not with hided num)',sum(computer[1:]))
                print()
            else:
                'You haven\'t any bombs left!'



    print('Show cards!')
    print("computer's card:",computer,'the sum of them are',sum(computer))
    print('='*100)
    print(user_name+'\'s card:',player,'the sum of them are',sum(player))


    # whether player win or not
    if sum(computer) <= 21 and sum(player) <= 21:
        if sum(computer) < sum(player):
            print('YOU WIN!')
            points = points + 500
            print('Your points are',points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
        elif sum(computer) == sum(player):
            print('The score is tied')
            print('Your points are', points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
        else:
            print('YOU LOSE!')
            points = points - 300
            print('Your points are', points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
    elif sum(computer) > 21 and sum(player) > 21:
        if sum(computer) > sum(player):
            print('YOU WIN!')
            points = points + 500
            print('Your points are', points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
        elif sum(computer) == sum(player):
            print('The score is tied')
            print('Your points are', points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
        else:
            print('YOU LOSE!')
            points = points - 300
            print('Your points are', points)
            buy_bonus()
            buy_bomb()
            print('You have', put_back, 'put-backs left')
            print('You have', bombs, 'bombs left')
            started = True
            start_game('TBZmang')
    elif sum(computer) > 21 and sum(player) <= 21:
        print('YOU WIN!')
        points = points + 500
        print('Your points are', points)
        buy_bonus()
        buy_bomb()
        print('You have', put_back, 'put-backs left')
        print('You have', bombs, 'bombs left')
        started = True
        start_game('TBZmang')
    else:
        print('YOU LOSE!')
        points = points - 300
        print('Your points are', points)
        buy_bonus()
        buy_bomb()
        print('You have', put_back, 'put-backs left')
        print('You have', bombs, 'bombs left')
        started = True
        start_game('TBZmang')



start_game('TBZmang')
