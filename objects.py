class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def reveal_card(self):
        return self.number + " " + self.suit


class GameSplit:
    def __init__(self, one_hand, two_hand):
        self.player_one_hand = one_hand
        self.player_two_hand = two_hand
        self.faces = {"J": 1, "Q": 2, "K": 3, "A": 4}

    def show_hands(self):
        print("Player One Hand\n")
        print([card.reveal_card() for card in self.player_one_hand])
        print("Player Two Hand\n")
        print([card.reveal_card() for card in self.player_two_hand])

    def run_game(self):
        first = input("Would you like to go first (y/n): ")

        players_turn = 0

        if first == "y":
            players_turn = 1
        elif first == "n":
            players_turn = 2
        else:
            print("Must enter either y or n")

        print("Great!")
        print("For your go press enter to place your next card")

        print("\nPress enter to start: ")

        playing = True
        first_go = True
        previous_card = None
        while playing:
            try:
                if players_turn == 1:
                    # User's go
                    print("Player's go...")
                    holder = input("")
                    current_card = self.player_one_hand.pop()

                    if current_card != None:
                        print(current_card.reveal_card())
                        if not first_go:

                            if previous_card.number in list(self.faces.keys()):
                                for i in range(self.faces.get(previous_card.number)):
                                    print(i)
                        players_turn = 2
                        previous_card = current_card
                        first_go = False
                else:
                    # Computer's go
                    print("Computer's go...")
                    current_card = self.player_two_hand.pop()
                    if current_card != None:
                        print(current_card.reveal_card())
                        players_turn = 1
                        previous_card = current_card

            except IndexError:
                print("Game has ended")
                playing = False
