from objects import Card, GameSplit
import random


def generate_split(no_people):
    # Splits the deck into equal sized packs of the number of people playing

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    numbers = ['2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = [Card(rank, suit) for suit in suits for rank in numbers]

    card_frequency = {card: 0 for card in cards}

    player_one_hand = []
    player_two_hand = []

    counter = 0
    while counter != 52:
        random_index = random.randint(0, 51)
        card_in_question = cards[random_index]
        if card_frequency[card_in_question] == 0:
            random_number = random.randint(0, 1)
            threshold = 1 / no_people

            # Build 2 case for now

            # Assign to a hand
            if random_number <= threshold:
                player_one_hand.append(card_in_question)
            else:
                player_two_hand.append(card_in_question)

            card_frequency[card_in_question] += 1
            counter += 1

    return GameSplit(player_one_hand, player_two_hand)


def start_game_against_computer():
    splitting = generate_split(2)
    splitting.run_game()


def start_game_with_humans(no_players):
    pass


def menu():
    # This function runs the menu for the terminal game
    computer_or_not = input("Do you want to play against the computer (y/n): ")
    if computer_or_not == "y":
        start_game_against_computer()
    elif computer_or_not == "n":
        no_players = int(input("How many players are there: "))
        start_game_with_humans(no_players)
    else:
        print("Must enter either y or n... ")


menu()
