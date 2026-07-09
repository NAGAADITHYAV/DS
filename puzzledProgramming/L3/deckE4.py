"""Card and deck models used by the card trick."""

import random
from dataclasses import dataclass


SUITS = ("C", "D", "H", "S")
RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
SUIT_SYMBOLS = {
    "C": "♣",
    "H": "♥",
    "S": "♠",
    "D": "♦",
}


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __str__(self) -> str:
        return f"{SUIT_SYMBOLS[self.suit]} {self.rank}"

    def print_card(self) -> None:
        print(self)


class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(rank, suit)
            for rank in RANKS
            for suit in SUITS
        ]
        self._cards_by_code = {
            (card.rank, card.suit): card
            for card in self.cards
        }

    def get_cards(self) -> list[Card]:
        return random.sample(self.cards, 4)

    def distance(self, first_card: Card, second_card: Card) -> int:
        first_position = self.cards.index(first_card)
        second_position = self.cards.index(second_card)

        return (second_position - first_position) % len(self.cards)

    def get_card(self, first_card: Card, distance: int) -> Card:
        first_position = self.cards.index(first_card)
        second_position = (first_position + distance) % len(self.cards)

        return self.cards[second_position]

    @staticmethod
    def encode(bits: tuple[int, int, int, int]) -> int:
        if len(bits) != 4 or any(bit not in (0, 1) for bit in bits):
            raise ValueError("Expected a tuple of four bits")

        value = 0
        for bit in bits:
            value = value * 2 + bit

        return value

    @staticmethod
    def decode(value: int) -> tuple[int, int, int, int]:
        if value < 0 or value > 15:
            raise ValueError("Expected an integer from 0 to 15")

        return (
            value // 8 % 2,
            value // 4 % 2,
            value // 2 % 2,
            value % 2,
        )
