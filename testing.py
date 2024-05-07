# # river = [('ace', 'spades'), ('jack', 'spades'), (10, 'spades'), (7, 'hearts'), (3, 'spades')]
# #
# #
# # # def is_three_kind(card1, card2):
# # #     newriver = river
# # #     newriver.append(card1)
# # #     newriver.append(card2)
# # #     three_numbers = []
# # #     for i in range(len(river)):
# # #         three_kind = 0
# # #         for j in range(i+1, len(river)):
# # #             if river[i][0] == river[j][0]:
# # #                 three_kind += 1
# # #         if three_kind == 2:
# # #             three_numbers.append(river[i][0])
# # #             return True, three_numbers
# # #     return False
# # #
# # #
# # # print(is_three_kind((3, 'diamond'), (5, 'diamond')))
# #
# # def is_royal_flush(card1, card2):
# #     newriver = river
# #     newriver.append(card1)
# #     newriver.append(card2)
# #     card_numbers = []
# #     suits = []
# #     for card in river:
# #         card_numbers.append(card[0])
# #         suits.append(card[1])
# #     for suit in suits:
# #
# #     if 'ace' in card_numbers and 'king' in card_numbers and 'queen' in card_numbers and 'jack' in card_numbers and 10 in card_numbers :
# #
# #     return False
# #
# # print(is_royal_flush(('king', 'spades'), ('queen', 'spades')))
#
#
# river = [('Ace', 'Spades'), (5, 'Hearts'), (3, 'Spades'), (4, 'Spades')]
# card1 = (5, 'Spades')
# card2 = (2, 'Spades')
#
#
# def is_straight_flush():
#     river.append(card1)
#     river.append(card2)
#     newriver = face_convert()
#     is_straight = False
#     is_suited = False
#     high_card = None
#     possible_straight = []
#     card_numbers = []
#     s_counter = 0
#     for card in newriver:
#         card_numbers.append(card[0])
#     card_numbers.sort()
#     print(card_numbers)
#     for i in range(len(card_numbers)-4):
#         test_straight = []
#         card = card_numbers[i]
#         test_straight.append(newriver[i])
#         s_counter = 0
#         for x in range(1, 5):
#             if card_numbers[x] == card+x:
#                 test_straight.append(newriver[i+x])
#                 s_counter += 1
#         if s_counter == 4:
#             is_straight = True
#             possible_straight = test_straight
#             high_card = possible_straight[-1]
#             print('possible_straight', possible_straight)
#     suit = possible_straight[0][1]
#     for card in possible_straight:
#         if card[1] == suit:
#             is_suited = True
#         else:
#             is_suited = False
#             break
#
#     if is_suited == True and is_straight == True:
#         return True, high_card
#
#
def face_convert(list):
    faces = [('King', 13), ('Queen', 12), ('Jack', 11)]
    newlist = []
    for card in list:
        is_face = False
        for face in faces:
            if card[0] == face[0]:
                suit = card[1]
                newlist.append((face[1], suit))
                is_face = True
        if card[0] == 'Ace':
            suit = card[1]
            newlist.append((14, suit))
            newlist.append((1, suit))
            is_face = True
        elif not is_face:
            newlist.append(card)
    return newlist
#
#
# print(is_straight_flush())
from random import randint

cards = [('Ace', 'Hearts'), ('Ace', 'Diamonds'), ('Ace', 'Spades'), ('Ace', 'Clubs'), ('King', 'Hearts'),
         ('King', 'Diamonds'), ('King', 'Spades'), ('King', 'Clubs'), ('Queen', 'Hearts'), ('Queen', 'Diamonds'),
         ('Queen', 'Spades'), ('Queen', 'Clubs'), ('Jack', 'Hearts'), ('Jack', 'Diamonds'), ('Jack', 'Spades'),
         ('Jack', 'Clubs'), ('10', 'Hearts'), ('10', 'Diamonds'), ('10', 'Spades'), ('10', 'Clubs'),
         ('9', 'Hearts'), ('9', 'Diamonds'), ('9', 'Spades'), ('9', 'Clubs'), ('8', 'Hearts'),
         ('8', 'Diamonds'), ('8', 'Spades'), ('8', 'Clubs'), ('7', 'Hearts'), ('7', 'Diamonds'),
         ('7', 'Spades'), ('7', 'Clubs'), ('6', 'Hearts'), ('6', 'Diamonds'), ('6', 'Spades'),
         ('6', 'Clubs'), ('5', 'Hearts'), ('5', 'Diamonds'), ('5', 'Spades'), ('5', 'Clubs'),
         ('4', 'Hearts'), ('4', 'Diamonds'), ('4', 'Spades'), ('4', 'Clubs'), ('3', 'Hearts'),
         ('3', 'Diamonds'), ('3', 'Spades'), ('3', 'Clubs'), ('2', 'Hearts'), ('2', 'Diamonds'),
         ('2', 'Spades'), ('2', 'Clubs')]

river = []


def shuffle_cards():
    shuffled = []
    cards_shuffled = []
    for i in range(len(cards)):
        x = randint(0, 51)
        if x in cards_shuffled:
            while x in cards_shuffled:
                x = randint(0, 51)
        shuffled.append(cards[x])
    return shuffled


shuffled = shuffle_cards()


for num in range(5):
    randnum = randint(0, 51)
    river.append(shuffled[0])
    shuffled.remove(shuffled[0])

# card1 = shuffled[0]
# card2 = shuffled[1]






# def is_full_house(card1, card2):
#     river.append(card1)
#     river.append(card2)
#     newriver = river
#     three_numbers = []
#     three_kind = False
#     three_max = False
#     for i in range(len(newriver)):
#         three_kind = 0
#         for j in range(i + 1, len(newriver)):
#             if newriver[i][0] == newriver[j][0]:
#                 three_kind += 1
#         if three_kind == 2:
#             three_numbers.append(newriver[i][0])
#             three_kind = True
#             print('three of a kind')
#             break
#     if three_kind:
#         three_max = max(three_numbers)
#         for card in newriver:
#             if card[0] == three_numbers[0]:
#                 newriver.remove(card)
#     pair_numbers = []
#     pair = False
#     pair_max = None
#     for i in range(len(newriver)):
#         for j in range(i+1, len(newriver)):
#             print('comparing', newriver[i][0], 'and', newriver[j][0])
#             if newriver[i][0] == newriver[j][0]:
#                 print(newriver[i][0], 'and', newriver[j][0], 'are paired')
#                 pair_numbers.append(newriver[i][0])
#             if len(pair_numbers) > 0:
#                 pair = True
#                 print('pair')
#                 pair_max = pair_numbers[0]
#     if len(pair_numbers) == 2:
#         pair_max = max(pair_numbers)
#     if three_kind and pair:
#         return True, three_max, pair_max
#     return False

river = [(5, 'Clubs'), (4, 'Diamonds'), ('Ace', 'Hearts'), ('Ace', 'Spades'), (2, 'Clubs')]
card1 = ('King', 'Hearts')
card2 = (6, 'Diamonds')


# def is_straight(card1, card2):
#     newriver = river
#     newriver.append(card1)
#     newriver.append(card2)
#     newriver = face_convert(newriver)
#     card_numbers = []
#     is_straight_tf = False
#     straight_count = 0
#     straight_high = None
#     for card in newriver:
#         card_numbers.append(card[0])
#     card_numbers.sort()
#     for i in range(len(card_numbers)-4):
#         card = card_numbers[i]
#         possible_straight = [card]
#         for j in range(1, 5):
#             if card+j == card_numbers[i+j]:
#                 possible_straight.append(card_numbers[i+j])
#         if len(possible_straight) == 5:
#             is_straight_tf = True
#             straight_high = possible_straight[-1]
#     return is_straight_tf, straight_high
#
#
# print(is_straight(card1, card2))


# def is_quads(card1, card2):
#     newriver = river
#     newriver.append(card1)
#     newriver.append(card2)
#     quad_number = None
#     is_quad = False
#     for i in range(len(newriver)):
#         quad_number = newriver[i][0]
#         quadcounter = 0
#         for j in range(len(newriver)):
#             if newriver[j][0] == quad_number:
#                 quadcounter += 1
#         if quadcounter == 4:
#             is_quad = True
#             quad_number = newriver[i][0]
#             break
#         else:
#             quad_number = None
#             is_quad = False
#     return is_quad, quad_number
#
#
# x = is_quads(card1, card2)
# print(x)

# def is_pair(card1, card2):
#     newriver = river
#     newriver.append(card1)
#     newriver.append(card2)
#     pair_counter = 0
#     pair_numbers = []
#     paired = False
#     for i in range(len(newriver)):
#         for j in range(i+1, len(newriver)):
#             if newriver[i][0] == newriver[j][0]:
#                 print('pair found %s %s' % (newriver[i][0], newriver[j][0]))
#                 pair_counter += 1
#                 pair_numbers.append(newriver[i][0])
#                 paired = True
#                 break
#
#     return paired, pair_numbers


newriver = [(6, 'Hearts'), (6, 'Diamonds'), ('Jack', 'Diamonds'), ('Ace', 'Diamonds'), (8, 'Diamonds'), ('Ace', 'Diamonds')]

card_suits = []

for card in newriver:
    card_suits.append(card[1])
spades = 0
diamonds = 0
hearts = 0
clubs = 0
for suit in card_suits:
    if suit.lower() == 'spades':
        spades += 1
    elif suit.lower() == 'diamonds':
        diamonds += 1
    elif suit.lower() == 'hearts':
        hearts += 1
    elif suit.lower() == 'clubs':
        clubs += 1
    else:
        raise KeyError('Suit could not be calculated')

suits = {'spades': spades,
         'clubs': clubs,
         'diamonds': diamonds,
         'hearts': hearts}

for suit, count in suits.items():
    if count == 5:
        suit = suit.capitalize()
        print('True')
        print(suit)
