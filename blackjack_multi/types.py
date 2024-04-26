from enum import Enum

from pydantic import BaseModel


class RulesI(BaseModel):
    dealer_hit_soft17: bool = False
    push_dealer22: bool = False
    double_after_split: bool = True
    hit_after_split_aces: bool = False
    reduced_blackjack_payout: bool = False
    allow_surrender: bool = True
    split_any_ten: bool = True


class DeckI(BaseModel):
    shrink_deck: bool = True
    n_decks: int = 6
    ratio_penetrate: float = 4 / 6


class GameParamsI(DeckI):
    rules: RulesI


class SuitEnum(Enum):
    hearts = "H"
    clubs = "C"
    diamonds = "D"
    spades = "S"
