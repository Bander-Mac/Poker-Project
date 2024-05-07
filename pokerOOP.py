from time import sleep
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


def shuffle_cards(deck):
    shuffled = []
    cards_shuffled = []
    for i in range(len(deck)):
        x = randint(0, 51)
        if x in cards_shuffled:
            while x in cards_shuffled:
                x = randint(0, 51)
        shuffled.append(deck[x])
    return shuffled


def face_convert(cards):
    face_values = {'King': 13, 'Queen': 12, 'Jack': 11, 'Ace': [14, 1]}
    new_list = []
    for card in cards:
        if card[0] in face_values:
            suit = card[1]
            if card[0] == 'Ace':
                new_list.extend([(value, suit) for value in face_values['Ace']])
            else:
                new_list.append((face_values[card[0]], suit))
        else:
            new_list.append(card)
    return new_list


def face_unconverted(card):
    if card == 11:
        return 'Jack'
    elif card == 12:
        return 'Queen'
    elif card == 13:
        return 'King'
    elif card == 14 or card == 1:
        return 'Ace'
    else:
        return card


class Game:
    players = []

    def __init__(self):
        self.active = None
        self.starting_amount = 0
        self.username = None
        self.pot = 0
        self.call = 0
        self.river = []
        self.deck = shuffle_cards(cards)
        self.positions = ['Small Blind', 'Big Blind', 'UTG', 'Button', 'Hi-Jack', 'Lo-Jack']
        self.previous = None

    def play(self):
        self.username = input('Enter your name: ')
        print("Hello, {}, welcome to python poker.".format(self.username))
        self.create_player(self.username)

        self.starting_amount = input("How much would you like to start with 100k, 50k, 10k, 5k: ")
        amounts = ["100k", "50k", "10k", "5k"]
        while self.starting_amount not in amounts:
            self.starting_amount = input(
                "Invalid option, please put amount exactly how label (no spaces) 100k, 50k, 10k, 5k: ")
        if self.starting_amount == "100k":
            self.starting_amount = 100000
        elif self.starting_amount == "50k":
            self.starting_amount = 50000
        elif self.starting_amount == "10k":
            self.starting_amount = 10000
        elif self.starting_amount == "5k":
            self.starting_amount = 5000
        sleep(1)
        print("Awesome your starting balance is,", self.starting_amount)
        sleep(.5)
        players = int(input("How many players would you like to compete with (upto 5)? "))
        print("Great! Generating players...")
        for i in range(players):
            self.create_player(f'Enemy {i}')
        self.positions = self.positions[:len(self.players)]
        self.assign_position()
        self.update_player_amounts(self.starting_amount)
        print("Moving to a table...")
        sleep(.5)
        return self.starting_amount

    def start_hand(self):
        for player in self.players:
            player.folded = False
            player.pot_met = True
        self.pot = 0
        self.call = 0
        self.river = []
        self.deck = shuffle_cards(cards)
        position = self.positions.pop()
        self.positions.append(position)
        return self.pot, self.call, self.river, self.deck, self.positions

    def current_hand(self):
        self.blinds_in()


    @classmethod
    def update_player_amounts(cls, amount):
        for player in cls.players:
            player.balance = amount

    @classmethod
    def create_player(cls, name):
        cls.players.append(Player(name))
        return Player(name)

    def assign_position(self):
        for index, player in enumerate(self.players):
            player.position = self.positions[index]

    def deal(self):
        for player in self.players:
            player.hand.append(self.deck.pop())
            player.hand.append(self.deck.pop())

    def options(self, player):
        self.previous = player
        if player.name == self.username:
            choice = input("What would you like to do? ")
            if self.call > 0 and choice.lower() == 'check':
                while choice.lower() == "check":
                    print('You cannot check currently.')
                    sleep(.25)
                    choice = input("What would you like to do? ")
                self.options(player)
            elif self.call == 0 and choice.lower() == "raise":
                while choice.lower() == "raise":
                    print('There is no call')
                    sleep(.25)
                    choice = input("What would you like to do? ")
                self.options(player)
            elif self.call > 0 and choice.lower() == "bet":
                while choice.lower() == 'bet':
                    print("There is already a call, but you can raise.")
                    sleep(.25)
                    choice = input("What would you like to do? ")
                self.options(player)
            elif choice.lower() == 'fold':
                return 'fold', self.previous
            elif choice.lower() == 'check':
                return 'check', self.previous
            elif choice.lower() == 'bet':
                amount = input("How much would you like to bet? ")
                if "all" in amount.lower():
                    return 'bet', 'all', self.previous
                else:
                    try:
                        amount = int(amount)
                    except ValueError:
                        raise ValueError("Please enter an integer or all")
                while not amount.is_integer():
                    amount = input("How much would you like to bet? ")
                    if "all" in amount.lower():
                        return 'bet', 'all', self.previous
                if amount.is_integer() and amount > self.previous.balance:
                    amount = 'all'
                return 'bet', amount, self.previous
            elif choice.lower() == 'raise':
                amount = input('How much would you like to raise? ')
                if "all" in amount.lower():
                    return 'raise', 'all', self.previous
                else:
                    try:
                        amount = int(amount)
                    except ValueError:
                        raise ValueError("Please enter an integer or all")
                while not amount.is_integer():
                    amount = input("How much would you like to raise? ")
                    if "all" in amount.lower():
                        return 'raise', 'all', self.previous
                if amount.is_integer() and amount > self.previous.balance:
                    amount = 'all'
                return 'raise', amount, self.previous
            elif choice.lower() == 'call':
                return 'call', self.previous
        else:
            num = randint(1, 100)
            amount = randint(500, 1550)
            if self.call == 0 and num <= 70:
                return 'check', self.previous
            elif self.call == 0 and num <= 90:
                if amount >= 1550 or amount > self.previous.balance:
                    amount = 'all'
                return 'bet', amount, self.previous
            elif self.call > 0 and num <= 60:
                return 'call', self.previous
            elif self.call > 0 and num <= 90:
                if amount > self.previous.balance:
                    amount = 'all'
                return 'raise', amount, self.previous

    def start_hand(self):
        print("Dealing cards...")
        self.deal()

        for player in self.players:
            if player.name == self.username:
                for card in player.hand:
                    print("Your cards: ", card)

    def hands(self, card1, card2):
        newriver = self.river
        newriver.append(card1)
        newriver.append(card2)
        spades = 0
        clubs = 0
        diamonds = 0
        hearts = 0
        suit = None
        is_suited = False

        card_numbers = []

        for card in newriver:
            card_numbers.append(card[0])

        is_straight = all(item in card_numbers for item in ['Ace', 'King', 'Queen', 'Jack', 10])

        for cards in newriver:
            if cards[0] in ['Ace', 'King', 'Queen', 'Jack', 10]:
                if 'Spades' in cards[1]:
                    spades += 1
                if 'Clubs' in cards[1]:
                    clubs += 1
                if 'Diamonds' in cards[1]:
                    diamonds += 1
                if 'Hearts' in cards[1]:
                    hearts += 1

        suits = {'spades': spades,
                 'clubs': clubs,
                 'diamonds': diamonds,
                 'hearts': hearts}

        for suit, count in suits.items():
            if count == 5:
                is_suited = True
                suit = suit.capitalize()
                break

        if is_suited and is_straight:
            return suit, 'royal flush'

        newriver = face_convert(newriver)
        spades = 0
        clubs = 0
        diamonds = 0
        hearts = 0
        is_straight = False
        is_suited = False
        high_card = None

        possible_straight = []
        card_numbers = []

        for card in newriver:
            card_numbers.append(card[0])
        card_numbers.sort()

        for i in range(len(card_numbers) - 4):
            test_straight = []
            card = card_numbers[i]
            test_straight.append(card_numbers[i])
            s_counter = 0
            for x in range(1, 5):
                if card_numbers[i + x] == card + x:
                    test_straight.append(card_numbers[i + x])
                    s_counter += 1
                else:
                    break
            if s_counter == 4:
                is_straight = True
                possible_straight = test_straight
                high_card = possible_straight[-1]

        for card in newriver:
            if card[0] in possible_straight:
                if 'Spades' in card[1]:
                    spades += 1
                if 'Clubs' in card[1]:
                    clubs += 1
                if 'Diamonds' in card[1]:
                    diamonds += 1
                if 'Hearts' in card[1]:
                    hearts += 1

        suits = {'spades': spades,
                 'clubs': clubs,
                 'diamonds': diamonds,
                 'hearts': hearts}

        for suit, count in suits.items():
            if count == 5:
                is_suited = True
                suit = suit.capitalize()
                break
        if is_suited == True and is_straight == True:
            return face_unconverted(high_card), 'straight-flush', suit

        newriver = face_convert(newriver)
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
            for j in range(i + 1, len(newriver)):
                if newriver[i][0] == newriver[j][0]:
                    pair_numbers.append(newriver[i][0])
                if len(pair_numbers) > 0:
                    pair = True
                    pair_max = pair_numbers[0]

        if len(pair_numbers) == 2:
            pair_max = max(pair_numbers)
        if three_kind and pair:
            return three_max, 'Full House', pair_max

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
                return suit, 'Flush'

        newriver = face_convert(newriver)
        card_numbers = []
        for card in newriver:
            card_numbers.append(card[0])
        card_numbers.sort()
        for i in range(len(card_numbers) - 4):
            card = card_numbers[i]
            possible_straight = [card]
            for j in range(1, 5):
                if card + j == card_numbers[i + j]:
                    possible_straight.append(card_numbers[i + j])
            if len(possible_straight) == 5:
                straight_high = possible_straight[-1]
                return face_unconverted(straight_high), 'straight'

        three_numbers = []
        for i in range(len(newriver)):
            three_kind = 0
            for j in range(i + 1, len(newriver)):
                if newriver[i][0] == newriver[j][0]:
                    three_kind += 1
                    if three_kind == 2:
                        three_numbers.append(newriver[i][0])
        if three_kind >= 2:
            return face_unconverted(max(face_convert(three_numbers))), 'three kind'

        pair_counter = 0
        pair_numbers = []
        paired = False
        for i in range(len(newriver)):
            for j in range(i + 1, len(newriver)):
                if newriver[i][0] == newriver[j][0]:
                    pair_counter += 1
                    pair_numbers.append(newriver[i][0])
                    paired = True
                    break

        if paired:
            return pair_numbers, 'pair'

    def hand_strength(self, hand):
        if not self.river:
            if hand[0][0] == hand[1][0]:
                pair_number = hand[0][0]
                return pair_number, 'pair'
        if self.river:
            for card in hand:
                self.river.append(card)
            river = self.river
            return 'river', river
        if self.river:
            for card in hand:
                self.river.append(card)

    def blinds_in(self):
        blind = self.starting_amount/25
        print('Blinds please put in your chips...')
        for player in self.players:
            if player.position == 'Small Blind':
                print(player.name, 'is small blind')
                player.balance -= blind
                self.pot += blind
            if player.position == 'Big Blind':
                print(player.name, 'is big blind')
                player.balance -= 2 * blind
                self.pot += 2 * blind
                self.previous = player
        return self.previous

    def active_player(self):
        for index, player in enumerate(self.players):
            if player == self.previous:
                self.active = self.players[index + 1]
                return self.active

    def show_players(self):
        for player in self.players:
            print(player.name)
            print(player.balance)
            print(player.position)

    def show_chips(self):
        for player in self.players:
            print(player.name, player.balance)

    def show_positions(self):
        for player in self.players:
            print(player.name, player.position)


class Player(Game):
    def __init__(self, name):
        super().__init__()
        self.hand = []
        self.name = name
        self.balance = self.starting_amount
        self.strength = self.hand_strength
        self.money_in = 0
        self.pot_met = True
        self.folded = False


if __name__ == '__main__':
    game = Game()
    game.play()
    game.start_hand()
    game.show_players()
    game.blinds_in()
    game.show_chips()
    game.active_player()
    game.options(game.active)





