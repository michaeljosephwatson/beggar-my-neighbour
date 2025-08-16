import time


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
        print("\nPlayer One Hand\n")
        print([card.reveal_card() for card in self.player_one_hand])
        print("\nPlayer Two Hand\n")
        print([card.reveal_card() for card in self.player_two_hand])

    def who_go_first(self):
        first = input("\nWould you like to go first (y/n): ")

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
        waiting_input = input("\nPlayer's turn: ")
        current_card = self.player_one_hand.pop()
        print()
        print(current_card.reveal_card())
        return current_card

    def remove_computer_card(self):
        time.sleep(0.5)
        current_card = self.player_two_hand.pop()
        print()
        print(current_card.reveal_card())
        return current_card

    def clear_deck(self, winner):
        if winner == 1:
            self.player_one_hand = self.current_deck + self.player_one_hand
            self.current_deck.clear()
        else:
            self.player_two_hand = self.current_deck + self.player_two_hand
            self.current_deck.clear()

    def evaluate_winner(self):
        if len(self.player_one_hand) == 0:
            print("\nPlayer one Wins!")
        else:
            print("\nComputer Wins!")

    def contest(self, cards_to_pull, player):
        for i in range(cards_to_pull):
            if player == 1:
                print(
                    f"\nPlayer needs to find a face in {cards_to_pull-i} cards")
                current_card = self.remove_player_card()
                self.current_deck.append(current_card)
                is_face, new_cards_to_pull = self.check_card(current_card)
                if is_face:
                    print("Face Card")
                    return self.contest(new_cards_to_pull, 2)
                else:
                    if i == cards_to_pull - 1:
                        print("Computer gets the deck!")
                        return 2, current_card
            else:
                print(
                    f"\nComputer needs to find a face in {cards_to_pull-i} cards")
                current_card = self.remove_computer_card()
                self.current_deck.append(current_card)
                is_face, new_cards_to_pull = self.check_card(current_card)
                if is_face:
                    print("Face Card")
                    return self.contest(new_cards_to_pull, 1)
                else:
                    if i == cards_to_pull - 1:
                        print("Player gets the deck!")
                        return 1, current_card

    def run_game(self):

        players_turn = self.who_go_first()

        print("\nGreat!")
        print("For your go press enter to place your next card")

        print("\nPress enter to start: ")

        playing = True
        previous_card = None
        while playing:

            try:
                if len(self.player_one_hand) == 0 or len(self.player_two_hand) == 0:
                    raise IndexError
                self.show_hands()

                if players_turn == 1:

                    if previous_card == None:
                        current_card = self.remove_player_card()
                        self.current_deck.append(current_card)
                        previous_card = current_card
                        players_turn = 2
                    else:
                        pullable, cards_to_pull = self.check_card(
                            previous_card)
                        if pullable:
                            winner, last_card = self.contest(cards_to_pull, 1)
                            players_turn = winner
                            self.clear_deck(winner)
                            previous_card = None

                        else:
                            current_card = self.remove_player_card()
                            self.current_deck.append(current_card)
                            previous_card = current_card
                            players_turn = 2

                else:
                    if previous_card == None:
                        print("\nComputer's turn: ")
                        current_card = self.remove_computer_card()
                        self.current_deck.append(current_card)
                        previous_card = current_card
                        players_turn = 1
                    else:
                        pullable, cards_to_pull = self.check_card(
                            previous_card)
                        if pullable:
                            winner, last_card = self.contest(cards_to_pull, 2)
                            players_turn = winner
                            self.clear_deck(winner)
                            previous_card = None
                        else:
                            print("\nComputer's turn: ")
                            current_card = self.remove_computer_card()
                            self.current_deck.append(current_card)
                            previous_card = current_card
                            players_turn = 1

            except IndexError:
                playing = False
                self.evaluate_winner()
