import random
# B Yashwanth Srinivasan: Python Project

# Generate deck of cards in a list
def generate_deck() -> list:
    suits = ['S', 'H', 'C', 'D']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [suit + value for suit in suits for value in values]
    return deck

# Distribute cards in a circular manner
def distribute_cards(deck: list, n_players: int) -> list:
    hands = [[] for _ in range(n_players)]
    for i, card in enumerate(deck):
        hands[i % n_players].append(card)
    for hand in hands:
        if not hand:
            hand.append(deck.pop(0))
    print(hands)
    return hands

# Function to check and correct the hands according the each play
def play_hand(hand: list, cards_on_the_table: list) -> bool:
    suits = ['S', 'H', 'C', 'D']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    if not hand:
        return True  # Player cannot play, they collect cards
    
    played_card = min((card for card in hand if card[:-1] == cards_on_the_table[0][:-1]), default=None)
    if played_card:
        hand.remove(played_card)
        cards_on_the_table.append(played_card)
        return False
    else:
        played_card = max(hand, key=lambda x: (values.index(x[1:]), suits.index(x[0])))
        hand.remove(played_card)
        cards_on_the_table.append(played_card)
        return True

# Function to simulate each round and check with play
def play_round(hands: list, starting_player: int) -> int:
    n_players = len(hands)
    if not hands[starting_player]:
        return (starting_player + 1) % n_players
    cards_on_the_table = [hands[starting_player].pop(0)]
    current_player = starting_player
    while True:
        current_player = (current_player + 1) % n_players
        if play_hand(hands[current_player], cards_on_the_table):
            return current_player

# Check the remaining hands
def n_remaining(hands):
    return sum(map(lambda x: len(x) > 0, hands))

# Function to simulate enire game and return loser and hands
def play_game(hands: list) -> tuple:
    n_players=len(hands)
    starting_player = next((i for i, hand in enumerate(hands) if 'SA' in hand), None)
    if starting_player is None:
        starting_player = random.randint(0, n_players - 1)
    current_player = starting_player

    while n_remaining(hands) > 1:
        current_player = play_round(hands, current_player)
        print(hands, "\n")

    loser = next(i for i, hand in enumerate(hands) if hand)
    return loser, hands

# Initialization and Running game
deck=generate_deck()
n_players = 5
random.seed()
random.shuffle(deck)
hands=distribute_cards(deck, n_players)
print("hands: ",hands)
loser, hand = play_game(hands)
print("Loser:", loser)
print("Hand:", hand)