import CardColorEnum as cc
import CardSymbolEnum as cs


class Card:
    def __init__(self, color, symbol):
        self.symbol = cs.CardSymbolEnum(symbol)
        self.color = cc.CardColorEnum(color)

    def getValue(self):
        if self.symbol == cs.CardSymbolEnum.Two:
            return 2
        elif self.symbol == cs.CardSymbolEnum.Three:
            return 3
        elif self.symbol == cs.CardSymbolEnum.Four:
            return 4
        elif self.symbol == cs.CardSymbolEnum.Five:
            return 5
        elif self.symbol == cs.CardSymbolEnum.Six:
            return 6
        elif self.symbol == cs.CardSymbolEnum.Seven:
            return 7
        elif self.symbol == cs.CardSymbolEnum.Eight:
            return 8  
        elif self.symbol == cs.CardSymbolEnum.Nine:
            return 9
        elif self.symbol == cs.CardSymbolEnum.Ace:
            return 11    
        else:
            return 10