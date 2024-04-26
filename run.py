from random import choice

from blackjack_pypi import Game

game = Game()

print("Count", game.count)
game.init_round(wagers=[1])
game.deal_init()

print("House Shows: ", (game.get_house_show().card, game.get_house_show().suit.name))

for i, player in enumerate(game.players):
    cur_hand = player.i_hand
    print("Player", i, "hand", cur_hand)
    print("\tCards: ", [
        (card.card, card.suit.name) for card in player.cards[cur_hand].cards
    ])
    while not player.is_done():
        moves = player.get_valid_moves()
        if "split" in moves:
            print("\tPlayer", i, "hand", cur_hand, "split")
            game.step_player(i, "split")
        else:
            move = choice(moves)
            print("\tPlayer", i, "hand", cur_hand, move)
            game.step_player(i, move)
        print("\t\tCards: ", [
            (card.card, card.suit.name) for card in player.cards[cur_hand].cards
        ])

game.step_house(only_reveal_card=True)
print("House Cards: ", [
        (card.card, card.suit.name) for card in game.house.cards[0].cards
    ])

while not game.house_done():
    print("House Draws Card")
    game.step_house()
    print("House Cards: ", [
        (card.card, card.suit.name) for card in game.house.cards[0].cards
    ])

print(game.get_results())

print()
print("Starting new round")
game.init_round([1, 1])
game.deal_init()

for i, player in enumerate(game.players):
    while not player.is_done():
        moves = player.get_valid_moves()
        if "split" in moves:
            game.step_player(i, "split")
        else:
            move = choice(moves)
            game.step_player(i, move)

game.step_house(only_reveal_card=True)
while not game.house_done():
    game.step_house()

print(game.get_results())
