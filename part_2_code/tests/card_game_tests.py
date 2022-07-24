import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        card = Card("heart", 1)
        self.assertEqual(True, CardGame.check_for_ace(card))
    
    def test_check_for_ace_non_ace(self):
        card = Card("spade", 5)
        self.assertEqual(False, CardGame.check_for_ace(card))

    def test_card_has_higher_value(self):
        card1 = Card("spade", 5)
        card2 = Card("club", 7)
        self.assertEqual(card2, CardGame.highest_card(card1, card2))
    
    def test_card_has_lower_value(self):
        card1 = Card("spade", 5)
        card2 = Card("club", 3)
        self.assertEqual(card1, CardGame.highest_card(card1, card2))
    
    
    def test_total_value_of_cards(self):
        cards = []
        card1 = Card("dimond", 5)
        card2 = Card("dimond", 6)
        card3 = Card("dimond", 7)
        card4 = Card("dimond", 3)
        card5 = Card("dimond", 8)
        card6 = Card("dimond", 9)
        card7 = Card("dimond", 10)
        cards.append(card1)
        cards.append(card2)
        cards.append(card3)
        cards.append(card4)
        cards.append(card5)
        cards.append(card6)
        cards.append(card7)
        self.assertEqual("You have a total of 48", CardGame.cards_total(cards))