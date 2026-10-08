import random


# ============================================================
# CARD CLASS
# ============================================================
# NEW OOP SECTION:
# A Card is an object.
#
# Instead of storing cards only as strings such as:
# "5 red"
#
# we create Card objects that contain:
# - value
# - colour
#
# This demonstrates:
# - Classes
# - Objects
# - Attributes
# - Methods
# ============================================================

class Card:

    def __init__(self, value, colour=None):
        # Store the value of the card.
        # Examples: "5", "skip", "reverse", "wildcard"
        self.value = value

        # Store the colour of the card.
        # Wildcards do not have a normal colour.
        self.colour = colour

    def __str__(self):
        # This method controls how the Card object
        # is displayed when we use print().
        #
        # Example:
        # Card("5", "red") -> "5 red"

        if self.colour is None:
            return self.value

        return self.value + " " + self.colour

    def is_wild(self):
        # This method checks whether the card is a wildcard.
        return self.value == "wildcard" or self.value == "wildcard draw4"


# ============================================================
# DECK CLASS
# ============================================================
# NEW OOP SECTION:
# The Deck class is responsible for creating,
# storing, shuffling and dealing cards.
#
# This demonstrates ENCAPSULATION because the deck's
# cards and operations are kept together inside the class.
# ============================================================

class Deck:

    def __init__(self):
        # Create an empty deck list.
        self.cards = []

        # Build the UNO deck when the Deck object is created.
        self.create_deck()

        # Shuffle the deck immediately.
        self.shuffle()

    # A DECK OF CARDS
    def create_deck(self):
        # define a function to make 108 cards for an uno deck
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "reverse", "skip", "draw2"]

        # create a list for the colour of cards
        colours = ["red", "blue", "yellow", "green"]

        # create an empty deck list
        self.cards = []

        # use a nested for loop
        for number in numbers:
            for colour in colours:
                # add a Card object to the deck
                self.cards.append(Card(number, colour))

                # since there is 4 zeros and two of each
                # of the other numbers add a condition to the loop
                if number != "0":
                    self.cards.append(Card(number, colour))

        # create a list for the wildcards
        wildcards = ["wildcard", "wildcard draw4"]

        # add the wildcards to the deck
        # note that there are 4 wildcards each so multiply by 4
        for wildcard in wildcards:
            for i in range(4):
                self.cards.append(Card(wildcard))

        # confirm if the number of cards stayed at 108
        print("Number of cards in deck:", len(self.cards))

    def shuffle(self):
        # to shuffle the deck of cards randomly
        random.shuffle(self.cards)

    def draw(self):
        # NEW OOP SECTION:
        # This method removes and returns one card from
        # the top of the deck.
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __len__(self):
        # NEW OOP SECTION:
        # This allows us to use len(deck)
        # instead of len(deck.cards).
        return len(self.cards)


# ============================================================
# PLAYER CLASS
# ============================================================
# NEW OOP SECTION:
# Each player is represented by a Player object.
#
# Each Player object has:
# - a name
# - a hand of cards
#
# This is another example of ENCAPSULATION.
# The player's cards and actions belong to the Player class.
# ============================================================

class Player:

    def __init__(self, name):
        # Store the player's name.
        self.name = name

        # Create an empty list for the player's cards.
        self.hand = []

    def receive_card(self, card):
        # Add a card to the player's hand.
        if card is not None:
            self.hand.append(card)

    def receive_cards(self, cards):
        # NEW OOP SECTION:
        # This allows the player to receive multiple cards.
        for card in cards:
            self.receive_card(card)

    def remove_card(self, index):
        # Remove and return a card from the player's hand.
        return self.hand.pop(index)

    def show_hand(self):
        # Display the player's cards with numbers.
        print()
        print("==========", self.name, "HAND ==========")

        for i, card in enumerate(self.hand):
            print(i, ":", card)

        print("================================")

    def has_won(self):
        # A player wins when they have no cards left.
        return len(self.hand) == 0

    def has_one_card(self):
        # Check whether the player has one card left.
        return len(self.hand) == 1

    def __len__(self):
        # Allow us to use len(player)
        # to get the number of cards.
        return len(self.hand)


# ============================================================
# DISCARD PILE CLASS
# ============================================================
# NEW OOP SECTION:
# The discard pile gets its own class.
#
# It is responsible for:
# - storing played cards
# - returning the top card
# - adding cards
# - reshuffling old cards
# ============================================================

class DiscardPile:

    def __init__(self):
        # Create an empty discard pile.
        self.cards = []

    def add_card(self, card):
        # Add a card to the discard pile.
        if card is not None:
            self.cards.append(card)

    def top_card(self):
        # Return the card currently on top.
        if len(self.cards) == 0:
            return None
        return self.cards[-1]

    def take_cards_for_reshuffle(self):
        # NEW OOP SECTION:
        # Keep the top card and return all older cards.
        #
        # The top card must remain visible during the game.
        if len(self.cards) <= 1:
            return []

        old_cards = self.cards[:-1]

        # Keep only the top card.
        self.cards = [self.cards[-1]]

        return old_cards

    def __len__(self):
        # Allow len(discard_pile).
        return len(self.cards)


# ============================================================
# UNO GAME CLASS
# ============================================================
# NEW OOP SECTION:
# This is the main class that controls the entire game.
#
# It contains:
# - the deck
# - the players
# - the draw pile
# - the discard pile
# - the current colour
# - the current player
#
# This demonstrates ENCAPSULATION because all the game's
# state and behaviour are contained inside UnoGame.
# ============================================================

class UnoGame:

    def __init__(self):
        # Create a new deck.
        self.deck = Deck()

        # Create the two players.
        self.playerH = Player("Player H")
        self.playerC = Player("Player C")

        # Create the discard pile.
        self.discard_pile = DiscardPile()

        # The draw pile will use the Deck object.
        self.draw_pile = self.deck

        # Player H starts the game.
        self.current_player = 0

        # The current colour will be determined
        # after the first card is placed.
        self.current_colour = None

    # ========================================================
    # DEAL CARDS
    # ========================================================
    # This replaces your original deal() function.
    #
    # The difference is that the method now works directly
    # with Player and Deck objects.
    # ========================================================

    def deal(self):
        # A hand of cards for 2 players & draw pile

        for i in range(7):
            # since each player gets 7 cards limit the range to 7
            # extract a card from the deck and give it to Player H
            self.playerH.receive_card(self.draw_pile.draw())

        print("--------------player H cards are ----------------")
        self.playerH.show_hand()

        # confirm that the player has 7 cards
        print("Number of Player H cards:", len(self.playerH))

        for i in range(7):
            # extract a card from the deck and give it to Player C
            self.playerC.receive_card(self.draw_pile.draw())

        print("---------------player C cards are----------")
        self.playerC.show_hand()

        print("Number of Player C cards:", len(self.playerC))

        # The remaining cards automatically become the draw pile.
        #
        # NEW OOP IMPROVEMENT:
        # We no longer need:
        #
        # for i in range(93):
        #     draw_pile.append(mydeck.pop())
        #
        # because the Deck object already contains the
        # remaining cards.

        print("----------The draw pile cards are-----------")
        print("Cards remaining:", len(self.draw_pile))

    # ========================================================
    # CREATE DISCARD PILE
    # ========================================================

    def create_discard_pile(self):
        # DICSARD PILE

        # Draw the first card from the draw pile.
        first_card = self.draw_pile.draw()

        # A Wild Draw 4 should not normally start the game.
        # If it appears, keep drawing until a normal card appears.
        while first_card is not None and first_card.value == "wildcard draw4":
            self.draw_pile.cards.insert(0, first_card)
            self.draw_pile.shuffle()
            first_card = self.draw_pile.draw()

        # Add the first card to the discard pile.
        self.discard_pile.add_card(first_card)

        print("--------This is the first card on the discard pile---------")
        print(self.discard_pile.top_card())
        print("Number of cards in discard pile:", len(self.discard_pile))

        # Set the starting colour.
        self.current_colour = self.discard_pile.top_card().colour
        print("Starting colour:", self.current_colour)

    # ========================================================
    # CHECK IF CARD CAN BE PLAYED
    # ========================================================

    def can_play(self, card):
        # Check that there is a card on the discard pile.
        top_card = self.discard_pile.top_card()

        if top_card is None:
            return True

        # Wildcards can always be played.
        if card.is_wild():
            return True

        # The card can be played if its colour matches.
        if card.colour == self.current_colour:
            return True

        # The card can also be played if its value matches.
        if card.value == top_card.value:
            return True

        return False

    # ========================================================
    # FIND PLAYABLE CARDS
    # ========================================================

    def get_playable_cards(self, player):
        # Look through a player's hand and find every card
        # that they are allowed to play.
        playable_cards = []

        for i, card in enumerate(player.hand):
            if self.can_play(card):
                playable_cards.append(i)

        return playable_cards

    # ========================================================
    # DRAW CARDS
    # ========================================================

    def draw_cards(self, player, amount):
        # Adds cards from the draw pile to a player's hand.
        for i in range(amount):
            card = self.draw_pile.draw()

            # If the draw pile is empty, try to refill it.
            if card is None:
                self.refill_draw_pile()
                card = self.draw_pile.draw()

            # If there are still no cards available,
            # stop drawing.
            if card is None:
                print("There are no more cards available.")
                return

            player.receive_card(card)

    # ========================================================
    # REFILL DRAW PILE
    # ========================================================

    def refill_draw_pile(self):
        # When the draw pile becomes empty, the old discard cards
        # are shuffled and become the new draw pile.
        old_cards = self.discard_pile.take_cards_for_reshuffle()

        if len(old_cards) == 0:
            return

        self.draw_pile.cards.extend(old_cards)
        self.draw_pile.shuffle()

        print()
        print("The discard pile has been reshuffled!")
        print("New draw pile:", len(self.draw_pile), "cards")

    # ========================================================
    # CHOOSE WILD CARD COLOUR
    # ========================================================

    def choose_colour(self):
        # Allows the player to choose a new colour after
        # playing a wildcard.
        colours = ["red", "blue", "yellow", "green"]

        while True:
            print()
            print("Choose a colour:")
            print("1 - red")
            print("2 - blue")
            print("3 - yellow")
            print("4 - green")

            choice = input("Enter your choice: ").lower().strip()

            if choice == "1" or choice == "red":
                return "red"
            elif choice == "2" or choice == "blue":
                return "blue"
            elif choice == "3" or choice == "yellow":
                return "yellow"
            elif choice == "4" or choice == "green":
                return "green"
            else:
                print("Invalid colour. Please try again.")

    # ========================================================
    # PLAY A CARD
    # ========================================================

    def play_card(self, player, card_index, chosen_colour=None):
        # Removes a card from a player's hand and puts it
        # onto the discard pile.
        card = player.remove_card(card_index)
        self.discard_pile.add_card(card)

        print()
        print(player.name, "played:", card)

        # Normal cards change the current colour.
        if not card.is_wild():
            self.current_colour = card.colour

        # Wildcards allow the player to choose a colour.
        else:
            if chosen_colour is None:
                self.current_colour = self.choose_colour()
            else:
                self.current_colour = chosen_colour

        return card

    # ========================================================
    # APPLY ACTION CARD
    # ========================================================

    def apply_action_card(self, card, other_player):
        # Handles reverse, skip, draw2 and wildcard draw4.

        if card.value == "reverse":
            print("Reverse card played!")
            print("With two players, Reverse skips the other player.")
            return True

        elif card.value == "skip":
            print("Skip card played!")
            print(other_player.name, "loses their turn.")
            return True

        elif card.value == "draw2":
            print("Draw 2 card played!")
            self.draw_cards(other_player, 2)
            print(other_player.name, "draws 2 cards.")
            return True

        elif card.value == "wildcard draw4":
            print("Wild Draw 4 played!")
            self.draw_cards(other_player, 4)
            print(other_player.name, "draws 4 cards.")
            return True

        return False

    # ========================================================
    # PLAYER TURN
    # ========================================================

    def play_turn(self, player, other_player):
        # Controls everything that happens during one turn.

        print()
        print("------------------------------------------")
        print(player.name, "'S TURN")
        print("------------------------------------------")

        print("Top card:", self.discard_pile.top_card())
        print("Current colour:", self.current_colour)

        player.show_hand()

        playable_cards = self.get_playable_cards(player)

        print()
        print("Playable card indexes:", playable_cards)

        # Ask the player what they want to do.
        while True:
            choice = input(
                "Enter the card number to play, D to draw, or Q to quit: "
            ).lower().strip()

            # QUIT
            if choice == "q":
                print("Game ended.")
                return "quit"

            # DRAW
            elif choice == "d":
                old_hand_size = len(player)
                self.draw_cards(player, 1)

                if len(player) > old_hand_size:
                    drawn_card = player.hand[-1]
                    print("You drew:", drawn_card)

                    # If the drawn card can be played,
                    # the player may choose to play it.
                    if self.can_play(drawn_card):
                        play_drawn = input(
                            "You can play this card. Play it? (y/n): "
                        ).lower().strip()

                        if play_drawn == "y":
                            card_index = len(player.hand) - 1
                            card = self.play_card(player, card_index)

                            skipped = self.apply_action_card(
                                card, other_player
                            )

                            if skipped:
                                return "skip"

                            return "played"

                # Turn ends after drawing.
                return "normal"

            # PLAY A CARD
            else:
                try:
                    card_index = int(choice)
                except ValueError:
                    print("Please enter a valid card number.")
                    continue

                if card_index < 0 or card_index >= len(player.hand):
                    print("That card number does not exist.")
                    continue

                selected_card = player.hand[card_index]

                if not self.can_play(selected_card):
                    print("You cannot play that card.")
                    print(
                        "The card must match the colour, "
                        "number/action, or be a wildcard."
                    )
                    continue

                card = self.play_card(player, card_index)

                skipped = self.apply_action_card(
                    card, other_player
                )

                if skipped:
                    return "skip"

                return "played"

    # ========================================================
    # CHECK WINNER
    # ========================================================

    def check_winner(self, player):
        # A player wins when their hand is empty.
        if player.has_won():
            print()
            print("==========================================")
            print("              GAME OVER!")
            print("==========================================")
            print(player.name, "WINS!")
            print("Congratulations!")
            print("==========================================")
            return True

        return False

    # ========================================================
    # UNO CHECK
    # ========================================================

    def check_uno(self, player):
        # Check whether the player has one card left.
        if player.has_one_card():
            print()
            print("==========================================")
            print("UNO!")
            print(player.name, "has one card left!")
            print("==========================================")

    # ========================================================
    # START GAME
    # ========================================================
    # This replaces the old "FLOW OF TURNS" section.
    #
    # The game continues until:
    # - someone wins
    # - someone quits
    # ========================================================

    def start_game(self):
        print()
        print("==========================================")
        print("             WELCOME TO UNO")
        print("==========================================")

        print("Player H and Player C will play.")

        # Deal 7 cards to each player.
        self.deal()

        # Create the starting discard card.
        self.create_discard_pile()

        # 0 means Player H's turn.
        # 1 means Player C's turn.
        self.current_player = 0

        # END OF GAME
        game_running = True

        while game_running:
            # PLAYER H TURN
            if self.current_player == 0:
                result = self.play_turn(
                    self.playerH,
                    self.playerC
                )

                if result == "quit":
                    game_running = False
                    continue

                if self.check_winner(self.playerH):
                    game_running = False
                    continue

                self.check_uno(self.playerH)

                if result == "skip":
                    self.current_player = 0
                else:
                    self.current_player = 1

            # PLAYER C TURN
            else:
                result = self.play_turn(
                    self.playerC,
                    self.playerH
                )

                if result == "quit":
                    game_running = False
                    continue

                if self.check_winner(self.playerC):
                    game_running = False
                    continue

                self.check_uno(self.playerC)

                if result == "skip":
                    self.current_player = 1
                else:
                    self.current_player = 0


# ============================================================
# CREATE AND RUN THE GAME
# ============================================================
# NEW OOP SECTION:
# Here we create an OBJECT from the UnoGame class.
#
# "game" is an object.
#
# Once we have the object, we call its start_game() method.
# ============================================================

if __name__ == "__main__":
    game = UnoGame()
    game.start_game()
