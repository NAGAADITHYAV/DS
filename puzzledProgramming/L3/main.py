"""Interactive entry point for the five-card trick."""

from assistantE2 import Assistant
from deck import Deck
from magician import Magician


def main() -> None:
    deck = Deck()
    assistant = Assistant(deck)
    magician = Magician(deck)

    while True:
        audience_cards = assistant.collect_audience_cards()
        shown_cards = assistant.arrange_four_cards(audience_cards)

        print("\nThe assistant shows these four cards:")
        for card in shown_cards:
            print(card)

        hidden_card = magician.predict_hidden_card(shown_cards)
        input("\nPress Enter when the magician is ready to reveal the hidden card...")
        print(f"The hidden card is {hidden_card}!")

        if input("\nDo you want to continue? (yes/no): ").strip().lower() == "no":
            break
        print()


if __name__ == "__main__":
    main()
