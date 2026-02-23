# deck_of_cards.py

> Unofficial Python wrapper for [deckofcardsapi.com](http://deckofcardsapi.com) — simulate a full deck of cards in your projects with ease.

---

## Quick Start

```python
from deck_of_cards import DeckOfCards

deck_of_cards = DeckOfCards()

# Shuffle a new deck and draw 5 cards
shuffled = deck_of_cards.shuffle_cards()
deck_id = shuffled["deck_id"]

hand = deck_of_cards.draw_card(deck_id=deck_id, count=5)
print(hand)
```

---

## Features

- 🃏 **Decks** — shuffle, create, reshuffle, partial decks with jokers
- 🎴 **Drawing** — draw from top, bottom, or at random
- 📦 **Piles** — create named piles, shuffle them, draw from them
- ♻️ **Return** — send cards back to the deck

---

## Usage

### Decks

```python
deck_of_cards = DeckOfCards()

# New shuffled deck (default 1 deck, up to 6)
result = deck_of_cards.shuffle_cards(deck_count=2)
deck_id = result["deck_id"]

# Brand new unshuffled deck
result = deck_of_cards.brand_new_deck(jokers_enabled=True)

# Partial deck with specific cards only
result = deck_of_cards.partial_deck(cards="AS,KS,QS,JS,10S")

# Reshuffle an existing deck
deck_of_cards.reshuffle_cards(deck_id=deck_id)

# Reshuffle only the remaining (undrawn) cards
deck_of_cards.reshuffle_cards(deck_id=deck_id, remaining=True)
```

### Drawing

```python
# Draw 1 card from the top (default)
deck_of_cards.draw_card(deck_id=deck_id)

# Draw multiple cards
deck_of_cards.draw_card(deck_id=deck_id, count=5)

# Draw from a brand new deck without creating one first
deck_of_cards.draw_card(deck_id="new", count=3)

# Draw from bottom or at random
deck_of_cards.draw_bottom(deck_id=deck_id)
deck_of_cards.draw_random(deck_id=deck_id)

# Return all drawn cards back to the deck
deck_of_cards.return_cards(deck_id=deck_id)
```

### Piles

Piles let you group cards into named stacks — useful for hands, discard piles, etc.

```python
# Add specific cards to a pile
deck_of_cards.add_to_pile(deck_id=deck_id, pile_name="player1", cards="AS,KD")

# List cards currently in a pile
deck_of_cards.list_pile(deck_id=deck_id, pile_name="player1")

# Shuffle a pile
deck_of_cards.shuffle_pile(deck_id=deck_id, pile_name="player1")

# Draw specific cards from a pile
deck_of_cards.draw_from_pile(deck_id=deck_id, pile_name="player1", cards="AS")

# Draw by count from a pile
deck_of_cards.draw_from_pile(deck_id=deck_id, pile_name="player1", count=2)
```

---

## API Reference

| Method           | Description                                  |
|------------------|----------------------------------------------|
| `shuffle_cards`  | Create and shuffle a new deck                |
| `brand_new_deck` | Create an unshuffled deck (jokers optional)  |
| `partial_deck`   | Shuffle a deck with specific cards only      |
| `reshuffle_cards`| Reshuffle an existing deck                   |
| `draw_card`      | Draw cards from the top                      |
| `draw_bottom`    | Draw a card from the bottom                  |
| `draw_random`    | Draw a random card                           |
| `return_cards`   | Return all drawn cards to the deck           |
| `add_to_pile`    | Add cards to a named pile                    |
| `shuffle_pile`   | Shuffle a named pile                         |
| `list_pile`      | List cards in a named pile                   |
| `draw_from_pile` | Draw cards from a pile by name or count      |

### Card codes

Cards are referenced by a two-character code: value + suit.

| Values | Suits |
|--------|-------|
| `A 2 3 4 5 6 7 8 9 10 J Q K` | `S` Spades · `D` Diamonds · `C` Clubs · `H` Hearts |

Examples: `AS` = Ace of Spades, `KH` = King of Hearts, `10C` = Ten of Clubs.

---
