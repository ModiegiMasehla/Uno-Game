# Uno-Game

A beginner-friendly UNO card game written in Python using Object-Oriented Programming (OOP).

## Features

- 108-card UNO deck
- Two players
- Seven cards dealt to each player
- Draw pile
- Discard pile
- Card matching by colour
- Card matching by number/action
- Wild card
- Wild Draw 4
- Skip
- Reverse
- Draw 2
- UNO notification
- Winner detection
- Draw pile reshuffling
- Unit tests using Python's `unittest` framework

## Project Structure

```text
uno_oop_project/
│
├── uno_game.py
├── README.md
└── tests/
    └── test_uno_game.py
```

## OOP Classes

### 1. Card

Represents one UNO card.

Attributes:
- `value`
- `colour`

Methods:
- `__str__()`
- `is_wild()`

### 2. Deck

Responsible for creating and managing the 108-card deck.

Methods:
- `create_deck()`
- `shuffle()`
- `draw()`

### 3. Player

Represents a player and their hand.

Methods:
- `receive_card()`
- `receive_cards()`
- `remove_card()`
- `show_hand()`
- `has_won()`
- `has_one_card()`

### 4. DiscardPile

Stores cards that have already been played.

Methods:
- `add_card()`
- `top_card()`
- `take_cards_for_reshuffle()`

### 5. UnoGame

Controls the complete game.

Responsibilities:
- Deal cards
- Create the starting discard card
- Check whether cards are playable
- Draw cards
- Reshuffle the discard pile
- Play cards
- Apply action cards
- Manage turns
- Check for UNO
- Check for a winner

## OOP Concepts Demonstrated

### Classes and Objects

Classes are blueprints.

For example:

```python
player = Player("Player H")
```

`player` is an object created from the `Player` class.

### Encapsulation

Data and behaviour are grouped together.

For example, a Player object stores its own hand:

```python
player.hand
```

and controls its own operations:

```python
player.receive_card(card)
player.remove_card(0)
```

### Abstraction

Complex operations are hidden behind simple methods.

For example:

```python
card = deck.draw()
```

The user of the Deck class does not need to know that `draw()` internally uses `pop()`.

### Composition

`UnoGame` is composed of other objects:

```text
UnoGame
├── Deck
├── Player
├── Player
└── DiscardPile
```

This is an important OOP design pattern.

## Running the Game

Make sure Python 3 is installed.

From the project directory:

```bash
python3 uno_game.py
```

On some systems you can use:

```bash
python uno_game.py
```

## Running the Tests

Run:

```bash
python3 -m unittest discover -s tests -v
```

You should see tests being executed with `OK` if they all pass.

You can also run:

```bash
python3 -m unittest tests/test_uno_game.py -v
```

## How to Play

When it is your turn, your cards will be displayed with indexes:

```text
========== Player H HAND ==========
0 : 5 red
1 : 7 blue
2 : skip green
3 : wildcard
================================
```

Enter the number of the card you want to play:

```text
0
```

Or draw a card:

```text
d
```

Or quit:

```text
q
```

If you draw a card that can be played, the game asks whether you want to play it.

## UNO Rules Implemented

A card can be played when:

1. It has the same colour as the current colour.
2. It has the same value/action as the top discard card.
3. It is a wildcard.

Special cards:

- `skip`: skips the other player.
- `reverse`: with two players, it behaves like a skip.
- `draw2`: other player draws two cards.
- `wildcard`: player chooses a colour.
- `wildcard draw4`: other player draws four cards and the player chooses a colour.

## Testing Approach

The project uses Python's built-in `unittest` framework.

Tests cover:

- Card creation
- Card string representation
- Wild cards
- Deck size
- Drawing from the deck
- Empty deck behaviour
- Player hands
- Removing cards
- Winner detection
- Discard pile
- Reshuffling
- Card matching
- Wildcards
- Drawing cards
- Playing cards
- Skip cards
- Draw 2 cards

## Learning Goals

This project is designed to demonstrate practical beginner/intermediate Python skills:

- Variables
- Lists
- Loops
- Conditional statements
- Functions
- Classes
- Objects
- Constructors
- Attributes
- Methods
- Encapsulation
- Abstraction
- Composition
- Unit testing
- Basic game state management

## Suggested Future Improvements

Possible future versions could add:

- 3–4 players
- Computer/AI player
- Proper turn-direction handling
- UNO penalty if a player fails to call UNO
- Score tracking
- Multiple rounds
- Save/load game
- Graphical user interface
- Better separation into multiple Python files
- `pytest` tests
- Type hints
- Dataclasses
- Custom exceptions