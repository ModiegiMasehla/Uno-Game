

import unittest

from uno_game import Card, Deck, Player, DiscardPile, UnoGame


class TestCard(unittest.TestCase):
    # ========================================================
    # CARD TESTS
    # ========================================================

    def test_card_stores_value_and_colour(self):
        card = Card("5", "red")

        self.assertEqual(card.value, "5")
        self.assertEqual(card.colour, "red")

    def test_card_string(self):
        card = Card("5", "red")

        self.assertEqual(str(card), "5 red")

    def test_wildcard_string(self):
        card = Card("wildcard")

        self.assertEqual(str(card), "wildcard")

    def test_wildcard_is_wild(self):
        card = Card("wildcard")

        self.assertTrue(card.is_wild())

    def test_draw4_is_wild(self):
        card = Card("wildcard draw4")

        self.assertTrue(card.is_wild())

    def test_normal_card_is_not_wild(self):
        card = Card("5", "red")

        self.assertFalse(card.is_wild())


class TestDeck(unittest.TestCase):
    # ========================================================
    # DECK TESTS
    # ========================================================

    def test_deck_has_108_cards(self):
        deck = Deck()

        self.assertEqual(len(deck), 108)

    def test_deck_draw_reduces_size(self):
        deck = Deck()

        original_size = len(deck)

        card = deck.draw()

        self.assertIsNotNone(card)
        self.assertEqual(len(deck), original_size - 1)

    def test_empty_deck_returns_none(self):
        deck = Deck()

        deck.cards.clear()

        self.assertIsNone(deck.draw())


class TestPlayer(unittest.TestCase):
    # ========================================================
    # PLAYER TESTS
    # ========================================================

    def test_player_starts_with_empty_hand(self):
        player = Player("Player H")

        self.assertEqual(len(player), 0)

    def test_player_receives_card(self):
        player = Player("Player H")
        card = Card("5", "red")

        player.receive_card(card)

        self.assertEqual(len(player), 1)
        self.assertEqual(player.hand[0], card)

    def test_player_receives_multiple_cards(self):
        player = Player("Player H")

        cards = [
            Card("1", "red"),
            Card("2", "blue"),
            Card("3", "green")
        ]

        player.receive_cards(cards)

        self.assertEqual(len(player), 3)

    def test_remove_card(self):
        player = Player("Player H")
        card = Card("5", "red")

        player.receive_card(card)

        removed_card = player.remove_card(0)

        self.assertEqual(removed_card, card)
        self.assertEqual(len(player), 0)

    def test_player_has_won_with_empty_hand(self):
        player = Player("Player H")

        self.assertTrue(player.has_won())

    def test_player_has_not_won_with_cards(self):
        player = Player("Player H")
        player.receive_card(Card("5", "red"))

        self.assertFalse(player.has_won())

    def test_player_has_one_card(self):
        player = Player("Player H")
        player.receive_card(Card("5", "red"))

        self.assertTrue(player.has_one_card())


class TestDiscardPile(unittest.TestCase):
    # ========================================================
    # DISCARD PILE TESTS
    # ========================================================

    def test_discard_pile_starts_empty(self):
        discard = DiscardPile()

        self.assertEqual(len(discard), 0)

    def test_add_card(self):
        discard = DiscardPile()
        card = Card("5", "red")

        discard.add_card(card)

        self.assertEqual(len(discard), 1)
        self.assertEqual(discard.top_card(), card)

    def test_top_card(self):
        discard = DiscardPile()

        first = Card("5", "red")
        second = Card("7", "blue")

        discard.add_card(first)
        discard.add_card(second)

        self.assertEqual(discard.top_card(), second)

    def test_reshuffle_keeps_top_card(self):
        discard = DiscardPile()

        first = Card("1", "red")
        second = Card("2", "blue")
        top = Card("3", "green")

        discard.add_card(first)
        discard.add_card(second)
        discard.add_card(top)

        old_cards = discard.take_cards_for_reshuffle()

        self.assertEqual(len(old_cards), 2)
        self.assertEqual(discard.top_card(), top)
        self.assertEqual(len(discard), 1)


class TestUnoGame(unittest.TestCase):
    # ========================================================
    # UNO GAME TESTS
    # ========================================================

    def setUp(self):
        # Create a fresh game before each test.
        self.game = UnoGame()

        # Remove the automatically created cards from the
        # players and discard pile so each test can control
        # the game state.
        self.game.playerH.hand.clear()
        self.game.playerC.hand.clear()
        self.game.draw_pile.cards.clear()
        self.game.discard_pile.cards.clear()

    def test_game_has_two_players(self):
        self.assertEqual(self.game.playerH.name, "Player H")
        self.assertEqual(self.game.playerC.name, "Player C")

    def test_card_can_be_played_by_matching_colour(self):
        top_card = Card("5", "red")
        playable_card = Card("8", "red")

        self.game.discard_pile.add_card(top_card)
        self.game.current_colour = "red"

        self.assertTrue(self.game.can_play(playable_card))

    def test_card_can_be_played_by_matching_value(self):
        top_card = Card("5", "red")
        playable_card = Card("5", "blue")

        self.game.discard_pile.add_card(top_card)
        self.game.current_colour = "red"

        self.assertTrue(self.game.can_play(playable_card))

    def test_wrong_card_cannot_be_played(self):
        top_card = Card("5", "red")
        wrong_card = Card("8", "blue")

        self.game.discard_pile.add_card(top_card)
        self.game.current_colour = "red"

        self.assertFalse(self.game.can_play(wrong_card))

    def test_wildcard_can_always_be_played(self):
        top_card = Card("5", "red")
        wildcard = Card("wildcard")

        self.game.discard_pile.add_card(top_card)
        self.game.current_colour = "red"

        self.assertTrue(self.game.can_play(wildcard))

    def test_draw_cards(self):
        player = self.game.playerH

        self.game.draw_pile.cards = [
            Card("1", "red"),
            Card("2", "blue"),
            Card("3", "green")
        ]

        self.game.draw_cards(player, 2)

        self.assertEqual(len(player), 2)
        self.assertEqual(len(self.game.draw_pile), 1)

    def test_play_card_removes_card_from_hand(self):
        player = self.game.playerH

        card = Card("5", "red")

        player.receive_card(card)

        self.game.discard_pile.add_card(Card("2", "red"))
        self.game.current_colour = "red"

        played = self.game.play_card(player, 0)

        self.assertEqual(played, card)
        self.assertEqual(len(player), 0)
        self.assertEqual(self.game.discard_pile.top_card(), card)

    def test_check_winner(self):
        player = self.game.playerH

        self.assertTrue(self.game.check_winner(player))

    def test_player_with_cards_is_not_winner(self):
        player = self.game.playerH
        player.receive_card(Card("5", "red"))

        self.assertFalse(self.game.check_winner(player))

    def test_skip_card_returns_true(self):
        player = self.game.playerH
        other_player = self.game.playerC

        skip = Card("skip", "red")

        self.assertTrue(
            self.game.apply_action_card(skip, other_player)
        )

    def test_draw2_gives_two_cards(self):
        other_player = self.game.playerC

        self.game.draw_pile.cards = [
            Card("1", "red"),
            Card("2", "blue"),
            Card("3", "green")
        ]

        draw2 = Card("draw2", "red")

        self.game.apply_action_card(draw2, other_player)

        self.assertEqual(len(other_player), 2)


if __name__ == "__main__":
    unittest.main()
