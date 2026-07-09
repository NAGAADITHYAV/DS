"""Magician logic for decoding the four-card binary encoding trick."""

from collections import deque

from assistantE4 import Assistant, HIDDEN_CARD_MARKER, PlacedCard
from deckE4 import Card, Deck


class Magician:
    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    def predict_hidden_card(self, order: deque[PlacedCard]) -> Card:
        ordered_cards = list(order)
        first_card = self._find_first_card(ordered_cards)
        bits = self._decode_order(ordered_cards)
        distance = self.deck.encode(bits)

        return self.deck.get_card(first_card, distance)

    def _decode_order(
        self,
        ordered_cards: list[PlacedCard],
    ) -> tuple[int, int, int, int]:
        first_index = self._find_position(ordered_cards, 1)
        prediction_side = self._side_bit(
            self._find_position(ordered_cards, 2),
            first_index,
        )
        third_side = self._side_bit(
            self._find_position(ordered_cards, 3),
            first_index,
        )
        fourth_index = self._find_position(ordered_cards, 4)
        fourth_side = self._side_bit(fourth_index, first_index)
        reveal_fourth_card = 0

        if ordered_cards[fourth_index][1] != HIDDEN_CARD_MARKER:
            reveal_fourth_card = 1

        return (
            prediction_side,
            third_side,
            fourth_side,
            reveal_fourth_card,
        )

    @staticmethod
    def _find_first_card(ordered_cards: list[PlacedCard]) -> Card:
        for position, card in ordered_cards:
            if position == 1 and isinstance(card, Card):
                return card

        raise ValueError("Order must include the first revealed card")

    @staticmethod
    def _find_position(ordered_cards: list[PlacedCard], position: int) -> int:
        for index, (card_position, _) in enumerate(ordered_cards):
            if card_position == position:
                return index

        raise ValueError(f"Order must include position {position}")

    @staticmethod
    def _side_bit(card_index: int, first_index: int) -> int:
        if card_index > first_index:
            return 1
        return 0


if __name__ == "__main__":
    deck = Deck()
    assistant = Assistant(deck)
    magician = Magician(deck)
    order, answer = assistant.prepare_trick()
    prediction = magician.predict_hidden_card(order)

    print(f"Order: {list(order)}")
    print(f"Assistant answer: {answer}")
    print(f"Magician prediction: {prediction}")
    print(f"Correct: {prediction == answer}")
