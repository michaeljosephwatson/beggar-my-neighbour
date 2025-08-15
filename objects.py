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
        self.faces_score = {"J": 1, "Q": 2, "K": 3, "A": 4}
        self.faces = ["J", "Q", "K", "A"]
        self.current_deck = []

    def show_hands(self):
        print("Player One Hand\n")
        print([card.reveal_card() for card in self.player_one_hand])
        print("Player Two Hand\n")
        print([card.reveal_card() for card in self.player_two_hand])

    def who_go_first(self):
        first = input("Would you like to go first (y/n): ")

        players_turn = 0

        if first == "y":
            players_turn = 1
        elif first == "n":
            players_turn = 2
        else:
            print("Must enter either y or n")

        return players_turn

    def check_card(self, previous_card):
        if previous_card.number in self.faces:
            cards_to_pull = self.faces_score.get(previous_card.number)
            return True, cards_to_pull
        else:
            return False, -1

    def remove_player_card(self):
        waiting_input = input("")
        current_card = self.player_one_hand.pop()
        print()
        print(current_card.reveal_card())
        return current_card

    def remove_computer_card(self):
        waiting_input = input("")
        current_card = self.player_two_hand.pop()
        print()
        print(current_card.reveal_card())
        return current_card

    def contest(self, cards_to_pull, player):
        for i in range(cards_to_pull):
            if player == 1:
                print("Player's turn to pull...")
                current_card = self.remove_player_card()
                is_face, new_cards_to_pull = self.check_card(current_card)
                if is_face:
                    print("Face Card")
                    return self.contest(new_cards_to_pull, 2)
                else:
                    if i == cards_to_pull - 1:  # The last card and player has not been able to get a face card
                        print("Computer gets the deck.")
                        return 2, current_card
            else:
                print("Computer's turn to pull...")
                current_card = self.remove_computer_card()
                is_face, new_cards_to_pull = self.check_card(current_card)
                if is_face:
                    print("Face Card")
                    return self.contest(new_cards_to_pull, 1)
                else:
                    if i == cards_to_pull - 1:
                        print("Player gets the deck.")
                        return 1, current_card

    def run_game(self):

        players_turn = self.who_go_first()

        print("Great!")
        print("For your go press enter to place your next card")

        print("\nPress enter to start: ")

        playing = True
        previous_card = None
        while playing:
            try:
                if players_turn == 1:

                    if previous_card == None:
                        print("Player's turn...")
                        current_card = self.remove_player_card()
                        previous_card = current_card
                        players_turn = 2
                    else:
                        pullable, cards_to_pull = self.check_card(
                            previous_card)
                        if pullable:
                            winner, last_card = self.contest(cards_to_pull, 1)
                            players_turn = winner
                            previous_card = last_card

                        else:
                            print("Player's turn...")
                            current_card = self.remove_player_card()
                            previous_card = current_card
                            players_turn = 2

                else:
                    if previous_card == None:
                        print("Computer's turn...")
                        current_card = self.remove_computer_card()
                        previous_card = current_card
                        players_turn = 1
                    else:
                        pullable, cards_to_pull = self.check_card(
                            previous_card)
                        if pullable:
                            winner, last_card = self.contest(cards_to_pull, 2)
                            players_turn = winner
                            previous_card = last_card
                        else:
                            print("Computer's turn...")
                            current_card = self.remove_computer_card()
                            previous_card = current_card
                            players_turn = 1

            except IndexError:
                print("Game has ended")
                playing = False
