# Blackjack Gameplay

This is a python package for playing multiplayer blackjack. The modules retain state to allow for splits, doubles, surrenders, stay, and hit. Multiple players can play, can a single player can have > 1 hand due to splits.
Rules are flexible. By default, decks deplete until a stop card is hit. The module retains count, and manages rewards and possible actions.

## Overview

This comes with 3 main modules to work with, but Game wraps the other 2 and generally abstracts away the need to work with them directly.

## Example:

```
game = Game()

game.init_round([1, 1]) # 2 players, 1 unit each.
game.deal_init()

for i, player in enumerate(game.players):
    while not player.is_done():
        moves = player.get_valid_moves()
        # randomly take move, unless split is available.
        if "split" in moves:
            game.step_player(i, "split")
        else:
            move = choice(moves)
            game.step_player(i, move)

game.step_house(only_reveal_card=True)
while not game.house_done():
    game.step_house()

game.get_results()
```
