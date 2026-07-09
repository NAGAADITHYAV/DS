"""Assistant logic for the four-card binary encoding trick."""

from collections import deque

from deckE4 import Card, Deck


PREDICTION_CARD_MARKER = "P"
HIDDEN_CARD_MARKER = "H"

PlacedCard = tuple[int, Card | str]


class Assistant:
    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    def arrange_cards(self, cards: list[Card] | None = None) -> deque[PlacedCard]:
        """Choose hidden/shown cards and encode the prediction distance."""
        order, _ = self.prepare_trick(cards)
        return order

    def prepare_trick(
        self,
        cards: list[Card] | None = None,
    ) -> tuple[deque[PlacedCard], Card]:
        """Return the public card order and the real hidden prediction card."""
        if cards is None:
            cards = self.deck.get_cards()

        if len(cards) != 4 or len(set(cards)) != 4:
            raise ValueError("Exactly four unique cards are required")

        first_card, prediction_card, distance = self._choose_prediction_pair(cards)
        bits = self.deck.decode(distance)
        remaining_cards = [
            card
            for card in cards
            if card not in (first_card, prediction_card)
        ]
        third_card, fourth_card = remaining_cards

        order = deque([(1, first_card)])
        prediction_side, third_side, fourth_side, reveal_fourth_card = bits
        fourth_value = fourth_card if reveal_fourth_card else HIDDEN_CARD_MARKER

        self._place_card(order, prediction_side, (2, PREDICTION_CARD_MARKER))
        self._place_card(order, third_side, (3, third_card))
        self._place_card(order, fourth_side, (4, fourth_value))

        return order, prediction_card

    def _choose_prediction_pair(self, cards: list[Card]) -> tuple[Card, Card, int]:
        best_pair: tuple[Card, Card, int] | None = None

        for first_card in cards:
            for prediction_card in cards:
                if first_card == prediction_card:
                    continue

                distance = self.deck.distance(first_card, prediction_card)
                if distance > 13:
                    continue

                if best_pair is None or distance < best_pair[2]:
                    best_pair = first_card, prediction_card, distance

        if best_pair is None:
            raise ValueError("No two cards are within 13 positions")

        return best_pair

    @staticmethod
    def _place_card(
        order: deque[PlacedCard],
        side: int,
        placed_card: PlacedCard,
    ) -> None:
        if side == 1:
            order.append(placed_card)
        else:
            order.appendleft(placed_card)


if __name__ == "__main__":
    assistant = Assistant(Deck())
    print(assistant.arrange_cards())
