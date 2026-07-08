"""Card and deck models used by the card trick."""

from dataclasses import dataclass


SUITS = ("C", "H", "S", "D")
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
    rank_value: int

    def __str__(self) -> str:
        return f"{SUIT_SYMBOLS[self.suit]} {self.rank}"


class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(rank, suit, rank_value)
            for rank_value, rank in enumerate(RANKS, start=1)
            for suit in SUITS
        ]
        self._cards_by_code = {
            (card.rank, card.suit): card
            for card in self.cards
        }

    def get_card(self, rank: str, suit: str) -> Card:
        """Return a card from rank and suit codes such as ``6`` and ``C``."""
        try:
            return self._cards_by_code[(rank.upper(), suit.upper())]
        except KeyError as error:
            raise ValueError(f"Invalid card: {rank} {suit}") from error
