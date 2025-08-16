**Capstone Project - Beggar My Neighbour**

This is my python implementation of the game Beggar My Neighbour.

Rules of the game:
+ Players split the deck evenly
+ Players take turns laying cards down face-up on top of each other
+ If a face card is shown (Jack, King, Queen, Ace) then the other player must place the maximum amount of cards attempting to also get a face card.
    - Jack: 1 card
    - Queen: 2 cards
    - King: 3 cards
    - Ace: 4 cards
+ If the responding player does not get a face card then the player who placed the face card gets the pack.
+ The aim of the game is to get the whole pack.

Example interaction: 2 players, player 1 places a queen of hearts, player 2 then places a 3 of clubs and then a jack of spades, then player 1 places a 5 of diamonds. This is not a face card so player 2 takes the pack and then leads the next interaction.

Currently can play against the computer.

To play the game clone repository and run `python3 play_game.py'

