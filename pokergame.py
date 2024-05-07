from time import sleep
from random import randint


def face_convert(river_list):
    faces = [('King', 13), ('Queen', 12), ('Jack', 11)]
    for card in river_list:
        if card[0] == 'Ace':
            suit = card[1]
            river_list.remove(('Ace', suit))
            river_list.append((14, suit))
            river_list.append((1, suit))
        else:
            for face in faces:
                if card[0] == face[0]:
                    suit = card[1]
                    river_list.remove((face[0], suit))
                    river_list.append((face[1], suit))
    return river_list





def is_straight_flush(card1, card2):
    river.append(card1)
    river.append(card2)
    newriver = face_convert(river)
    is_straight = False
    is_suited = False
    high_card = None
    possible_straight = []
    card_numbers = []
    for card in newriver:
        card_numbers.append(card[0])
    card_numbers.sort()
    print(card_numbers)
    for i in range(len(card_numbers)-4):
        test_straight = []
        card = card_numbers[i]
        test_straight.append(newriver[i])
        s_counter = 0
        for x in range(1, 5):
            if card_numbers[x] == card+x:
                test_straight.append(newriver[i+x])
                s_counter += 1
        if s_counter == 4:
            is_straight = True
            possible_straight = test_straight
            high_card = possible_straight[-1]
            print('possible_straight', possible_straight)
    suit = possible_straight[0][1]
    for card in possible_straight:
        if card[1] == suit:
            is_suited = True
        else:
            is_suited = False
            break

    if is_suited == True and is_straight == True:
        return True, high_card, 'straight flush'


def is_quads(card1, card2):
    newriver = river
    newriver.append(card1)
    newriver.append(card2)
    quad_number = None
    is_quad = False
    for i in range(len(newriver)):
        quad_number = newriver[i][0]
        quadcounter = 0
        for j in range(len(newriver)):
            if newriver[j][0] == quad_number:
                quadcounter += 1
        if quadcounter == 4:
            is_quad = True
            quad_number = newriver[i][0]
            break
        else:
            quad_number = None
            is_quad = False
    return is_quad, quad_number, 'quads'


def is_full_house(card1, card2):
    river.append(card1)
    river.append(card2)
    newriver = river
    three_numbers = []
    three_kind = False
    three_max = False
    for i in range(len(newriver)):
        three_kind = 0
        for j in range(i + 1, len(newriver)):
            if newriver[i][0] == newriver[j][0]:
                three_kind += 1
        if three_kind == 2:
            three_numbers.append(newriver[i][0])
            three_kind = True
            print('three of a kind')
            break
    if three_kind:
        three_max = max(three_numbers)
        for card in newriver:
            if card[0] == three_numbers[0]:
                newriver.remove(card)
    pair_numbers = []
    pair = False
    pair_max = None
    for i in range(len(newriver)):
        for j in range(i+1, len(newriver)):
            print('comparing', newriver[i][0], 'and', newriver[j][0])
            if newriver[i][0] == newriver[j][0]:
                print(newriver[i][0], 'and', newriver[j][0], 'are paired')
                pair_numbers.append(newriver[i][0])
            if len(pair_numbers) > 0:
                pair = True
                print('pair')
                pair_max = pair_numbers[0]
    if len(pair_numbers) == 2:
        pair_max = max(pair_numbers)
    if three_kind and pair:
        return True, three_max, 'full house', pair_max
    return False


def is_flush(card1, card2):
    newriver = river
    newriver.append(card1)
    newriver.append(card2)
    card_suits = []
    for card in newriver:
        card_suits.append(card[1])
    is_spade = 0
    is_diamond = 0
    is_hearts = 0
    is_clubs = 0
    for suit in newriver:
        if suit.lower() == 'spade':
            is_spade += 1
        elif suit.lower() == 'diamond':
            is_diamond += 1
        elif suit.lower() == 'hearts':
            is_hearts += 1
        else:
            is_clubs += 1
    if is_spade == 5:
        return True, 'spade', 'flush'
    elif is_diamond == 5:
        return True, 'diamond', 'flush'
    elif is_clubs == 5:
        return True, 'clubs', 'flush'
    elif is_hearts == 5:
        return True, 'hearts', 'flush'
    else:
        return False


def is_straight(card1, card2):
    newriver = river
    newriver.append(card1)
    newriver.append(card2)
    newriver = face_convert(newriver)
    card_numbers = []
    is_straight_tf = False
    straight_high = None
    for card in newriver:
        card_numbers.append(card[0])
    card_numbers.sort()
    for i in range(len(card_numbers)-4):
        card = card_numbers[i]
        possible_straight = [card]
        for j in range(1, 5):
            if card+j == card_numbers[i+j]:
                possible_straight.append(card_numbers[i+j])
        if len(possible_straight) == 5:
            is_straight_tf = True
            straight_high = possible_straight[-1]
    return is_straight_tf, straight_high, 'straight'


def is_three_kind(card1, card2):
    newriver = river
    newriver.append(card1)
    newriver.append(card2)
    three_numbers = []
    for i in range(len(newriver)):
        three_kind = 0
        for j in range(i+1, len(newriver)):
            if newriver[i][0] == newriver[j][0]:
                three_kind += 1
        if three_kind == 2:
            three_numbers.append(newriver[i][0])
            return True, three_numbers, 'three kind'
    return False


def is_pair(card1, card2):
    newriver = river
    newriver.append(card1)
    newriver.append(card2)
    pair_counter = 0
    pair_numbers = []
    paired = False
    for i in range(len(newriver)):
        for j in range(i+1, len(newriver)):
            if newriver[i][0] == newriver[j][0]:
                pair_counter += 1
                pair_numbers.append(newriver[i][0])
                paired = True
                break

    return paired, pair_numbers, 'pair'




players = [
    ('user', [(), (), 0, 'small blind'], 'hasn\'t played'),
    ('enemy1', [(), (), 0, 'big blind'], 'hasn\'t played'),
    ('enemy2', [(), (), 0, 'utg'], 'hasn\'t played'),
    ('enemy3', [(), (), 0, 'middle position'], 'hasn\'t played'),
    ('enemy4', [(), (), 0, 'cut off'], 'hasn\'t played'),
    ('enemy5', [(), (), 0, 'dealer'], 'hasn\'t played')
]

river = []


def deal_cards(shuffled):
    player_number = -1
    for player in players:
        player_number += 1
        if "dealer" in player[1]:
            player[1][0] = shuffled.pop(0)
            if players[player_number] != players[-1]:
                players[player_number+1][1][0] = shuffled.pop(0)
                if players[player_number+1] != players[-1]:
                    players[player_number+2][1][0] = shuffled.pop(0)
                    if players[player_number+2] != players[-1]:
                        players[player_number+3][1][0] = shuffled.pop(0)
                        if players[player_number+3] != players[-1]:
                            players[player_number+4][1][0] = shuffled.pop(0)
                            if players[player_number+4] != players[-1]:
                                players[player_number+5][1][0] = shuffled.pop(0)
                                continue
                            else:
                                players[0][1][0] = shuffled.pop(0)
                                continue
                        else:
                            players[0][1][0] = shuffled.pop(0)
                            players[1][1][0] = shuffled.pop(0)
                            continue
                    else:
                        players[0][1][0] = shuffled.pop(0)
                        players[1][1][0] = shuffled.pop(0)
                        players[2][1][0] = shuffled.pop(0)
                        continue
                else:
                    players[0][1][0] = shuffled.pop(0)
                    players[1][1][0] = shuffled.pop(0)
                    players[2][1][0] = shuffled.pop(0)
                    players[3][1][0] = shuffled.pop(0)
                    continue
            else:
                players[0][1][0] = shuffled.pop(0)
                players[1][1][0] = shuffled.pop(0)
                players[2][1][0] = shuffled.pop(0)
                players[3][1][0] = shuffled.pop(0)
                players[4][1][0] = shuffled.pop(0)
                continue
    for player in players:
        if "dealer" in player[1]:
            player[1][1] = shuffled.pop(1)
            if players[player_number] != players[-1]:
                players[player_number + 1][1][1] = shuffled.pop(1)
                if players[player_number + 1] != players[-1]:
                    players[player_number + 2][1][1] = shuffled.pop(1)
                    if players[player_number + 2] != players[-1]:
                        players[player_number + 3][1][1] = shuffled.pop(1)
                        if players[player_number + 3] != players[-1]:
                            players[player_number + 4][1][1] = shuffled.pop(1)
                            if players[player_number + 4] != players[-1]:
                                players[player_number + 5][1][1] = shuffled.pop(1)
                                continue
                            else:
                                players[0][1][1] = shuffled.pop(1)
                                continue
                        else:
                            players[0][1][1] = shuffled.pop(1)
                            players[1][1][1] = shuffled.pop(1)
                            continue
                    else:
                        players[0][1][1] = shuffled.pop(1)
                        players[1][1][1] = shuffled.pop(1)
                        players[2][1][1] = shuffled.pop(1)
                        continue
                else:
                    players[0][1][1] = shuffled.pop(1)
                    players[1][1][1] = shuffled.pop(1)
                    players[2][1][1] = shuffled.pop(1)
                    players[3][1][1] = shuffled.pop(1)
                    continue
            else:
                players[0][1][1] = shuffled.pop(1)
                players[1][1][1] = shuffled.pop(1)
                players[2][1][1] = shuffled.pop(1)
                players[3][1][1] = shuffled.pop(1)
                players[4][1][1] = shuffled.pop(1)
                continue


def options(previous, next_player):
    choices = ['check', 'fold', 'raise', 'help', 'quit']
    choice = input('What would you like to do (if you don\'t know what your options are type "help"): ')
    while choice not in choices:
        choice = input('I don\'t understand... what did you say? (if you don\'t know your options type "help"): ')
    if previous.lower() == 'raise':
        while choice == 'check':
            choice = input('Checking is not available in this position (if you don\'t know your options type "help"): ')
    if choice == 'check':
        print('Checking to {}...'.format(next_player))
        return 'check'
    if choice == 'raise':
        amount = input('How much are you raising?: ')
        print('Raising to', amount)
        return 'raise', amount
    if choice == 'fold':
        print('folding...')
    return 'fold'


def flop(deck):
    deck.pop()
    for i in range(3):
        river.append(deck.pop())


def check_hand(card1, card2, river):
    if len(river) >= 3:
        if is_royal_flush(card1, card2):
            return is_royal_flush(card1, card2)
        if is_straight_flush(card1, card2):
            return is_straight_flush(card1, card2)
        if is_quads(card1, card2):
            return is_quads(card1, card2)
        if is_full_house(card1, card2):
            return is_full_house(card1, card2)
        if is_flush(card1, card2):
            return is_flush(card1, card2)
        if is_straight(card1, card2):
            return is_straight(card1, card2)
        if is_three_kind(card1, card2):
            return is_three_kind(card1, card2)
        if is_pair(card1, card2):
            return is_pair(card1, card2)
        else:
            river.append(card1)
            river.append(card2)
            river = face_convert(river)
            return 'High Card', max(river)
    elif len(river) == 0:
        paired, pair_number, pair = is_pair(card1, card2)
        if paired:
            return paired, pair_number, pair
        else:
            card1 = face_convert([card1])
            card2 = face_convert([card2])
            return max([card1, card2])


def start_hand(starting_amount, pot, call):
    small_blind = int(starting_amount/100)
    big_blind = int(starting_amount/50)
    print('Blinds please go in.')
    for index, player in enumerate(players):
        if player[1][3] == 'small blind':
            print(player[0], 'is small blind, putting in', small_blind)
            pot += small_blind
        elif player[1][3] == 'big blind':
            print(player[0], 'is big blind, putting in', big_blind)
            next_player = players[index+1]
            pot += big_blind
            call = big_blind
            return next_player, pot, call


def next_player(player):
    strength = check_hand(player[1][0], player[1][1], river)
    hand = strength[3]
    numbers = strength[2]


def show_user_cards():
    for player in players:
        if player[0].lower() == 'user':
            print(player[1][0], player[1][1])


def main():
    pot = 0
    call = 0
    username = input("Enter your name: ")
    print("Hello, {}, welcome to python poker.".format(username))


    for player in players:
        player[1][2] = starting_amount
    sleep(1)
    print("Lets get to a table")
    sleep(1)
    print("Welcome, dealing cards...")

    shuffled = shuffle_cards()
    sleep(1)

    deal_cards(shuffled)
    print("Your Cards: ")

    show_user_cards()

    player, pot, call = start_hand(starting_amount, pot, call)



main()
