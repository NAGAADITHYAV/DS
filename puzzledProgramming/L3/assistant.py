"""Assistant logic for collecting and strategically arranging the cards."""

from deck import Card, Deck, RANKS, SUITS


class Assistant:
    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    def collect_audience_cards(self, count: int = 5) -> list[Card]:
        """Collect valid, non-duplicate cards from the audience."""
        cards: list[Card] = []
        print("Enter five cards as RANK SUIT (example: 6 C or K H).")

        while len(cards) < count:
            card_number = len(cards) + 1
            card_input = input(f"Card {card_number}: ").strip().upper().split()

            if len(card_input) != 2:
                print("Use the format RANK SUIT, for example: 6 C")
                continue

            rank, suit = card_input
            if rank not in RANKS or suit not in SUITS:
                print("Invalid card. Ranks: A, 2-10, J, Q, K; suits: C, H, S, D.")
                continue

            card = self.deck.get_card(rank, suit)
            if card in cards:
                print("That card has already been entered.")
                continue

            cards.append(card)

        return cards

    def arrange_four_cards(self, cards: list[Card]) -> list[Card]:
        """Hide one of five cards and encode it in the order of the other four."""
        if len(cards) != 5 or len(set(cards)) != 5:
            raise ValueError("Exactly five unique cards are required")

        same_suit_pair = self._find_same_suit_pair(cards)
        first_card, hidden_card, distance = self._choose_cards(same_suit_pair)
        remaining_cards = [card for card in cards if card not in same_suit_pair]
        encoded_cards = self._encode_distance(remaining_cards, distance)

        return [first_card, *encoded_cards]

    @staticmethod
    def _find_same_suit_pair(cards: list[Card]) -> tuple[Card, Card]:
        first_card_by_suit: dict[str, Card] = {}

        for card in cards:
            if card.suit in first_card_by_suit:
                return first_card_by_suit[card.suit], card
            first_card_by_suit[card.suit] = card

        raise ValueError("No two cards have the same suit")

    @staticmethod
    def _choose_cards(pair: tuple[Card, Card]) -> tuple[Card, Card, int]:
        lower_card, higher_card = sorted(pair, key=lambda card: card.rank_value)
        distance = higher_card.rank_value - lower_card.rank_value

        if distance <= 6:
            return lower_card, higher_card, distance

        return higher_card, lower_card, 13 - distance

    @staticmethod
    def _encode_distance(cards: list[Card], distance: int) -> list[Card]:
        low, middle, high = sorted(
            cards,
            key=lambda card: (card.rank_value, card.suit),
        )
        patterns = {
            1: [low, middle, high],
            2: [low, high, middle],
            3: [middle, low, high],
            4: [middle, high, low],
            5: [high, low, middle],
            6: [high, middle, low],
        }
        return patterns[distance]
