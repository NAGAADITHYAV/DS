"""Magician logic for decoding the assistant's four cards."""

from deck import Card, Deck, RANKS


class Magician:
    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    def predict_hidden_card(self, shown_cards: list[Card]) -> Card:
        """Calculate the hidden fifth card using only four shown cards."""
        if len(shown_cards) != 4 or len(set(shown_cards)) != 4:
            raise ValueError("Exactly four unique cards are required")

        first_card = shown_cards[0]
        distance = self.deck.decode_distance(shown_cards[1:])
        hidden_rank_value = (first_card.rank_value - 1 + distance) % 13 + 1
        hidden_rank = RANKS[hidden_rank_value - 1]

        return self.deck.get_card(hidden_rank, first_card.suit)
